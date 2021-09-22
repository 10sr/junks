#!/usr/bin/env python3
#
# Check latest GitHub actions releases.
#
# Requirements
# ============
#
# - `Python <https://www.python.org/>`_ 3.8 or later
# - `PyYAML <https://pypi.org/project/PyYAML/>`_ 5.3.1 or later
# - `requests <https://pypi.org/project/requests/>`_ 2.24.0 or later
# - `termcolor <https://pypi.org/project/termcolor/>`_ 1.1.0 or later
#
# Prerequisites
# =============
#
# You need to provide ``GITHUB_TOKEN`` env var to allow making requests to
# GitHub API v4. Simplest way to export token from ``~/.bashrc`` (or
# ``~/.profile``) file as,
#
# .. code-block:: bash
#
#     export GITHUB_TOKEN="..."
#
# Usage
# =====
#
# .. code-block:: bash
#
#     check-latest-actions.py WORKFLOW_YAML [WORKFLOW_YAML]
#

# https://gist.github.com/playpauseandstop/5044d5fea88aec49316bf78592db17de

import os
import sys
from contextlib import suppress
from pathlib import Path
from typing import cast, DefaultDict, List, NamedTuple, Optional, Set

import requests
import yaml
from termcolor import colored


API_URL = "https://api.github.com/graphql"
API_TOKEN = os.getenv("GITHUB_TOKEN")

GQL_LATEST_RELEASE = """
query getLatestRelease($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    releases(last: 1) {
      nodes {
        tagName
      }
    }
  }
}
"""

try:
    YAML_LOADER = yaml.CSafeLoader
except AttributeError:
    YAML_LOADER = yaml.SafeLoader  # type: ignore


class VersionDiff(NamedTuple):
    action: str
    current_version: Optional[str]
    latest_version: str

    @property
    def raw_action(self) -> str:
        return (
            f"{self.action}@{self.current_version}"
            if self.current_version
            else self.action
        )


def check_latest_version(
    session: requests.Session, *, value: str
) -> Optional[VersionDiff]:
    current_version: Optional[str] = None
    if "@" in value:
        action, current_version = value.split("@", 1)
    else:
        action = value

    if "/" not in value:
        print(
            colored(f"ERROR: Wrong action {value}. Skip...", "red"),
            file=sys.stderr,
        )
        return None

    owner, name = action.split("/", 1)
    latest_version = get_latest_version(session, owner=owner, name=name)
    if latest_version is None:
        print(
            colored(
                f"ERROR: Unable to fetch latest version of {action}. Skip...",
                "red",
            ),
            file=sys.stderr,
        )
        return None

    return VersionDiff(action, current_version, latest_version)


def get_latest_version(
    session: requests.Session, *, owner: str, name: str
) -> Optional[str]:
    with suppress(requests.RequestException, IndexError, KeyError, ValueError):
        with session.post(
            API_URL,
            json={
                "query": GQL_LATEST_RELEASE,
                "variables": {"owner": owner, "name": name},
            },
        ) as response:
            response.raise_for_status()
            data = response.json()
            return cast(
                str,
                data["data"]["repository"]["releases"]["nodes"][0]["tagName"],
            )

    return None


def print_diff(diff: VersionDiff, paths: List[Path]) -> None:
    if diff.current_version == diff.latest_version:
        print(
            f"{colored(diff.raw_action, 'green', attrs=['bold'])} is "
            "up-to-date\n"
        )
        return

    current_label = (
        f" (current version: {colored(diff.current_version, 'red')})"
        if diff.current_version
        else ""
    )
    print(
        f"{colored(diff.action, 'yellow', attrs=['bold'])} is outdated. "
        f"Latest version: {colored(diff.latest_version, 'green')}"
        f"{current_label}"
    )

    print("Affected files:")
    for path in sorted(item.absolute() for item in paths):
        print(f"  - {path}")
    print("")


def process_workflow_yaml(path: Path) -> Optional[Set[str]]:
    if not path.exists():
        return None

    try:
        content = yaml.load(path.read_bytes(), Loader=YAML_LOADER)
    except ValueError:
        return None

    actions: Set[str] = set()

    for job in (content.get("jobs") or {}).values():
        for step in job.get("steps") or {}:
            maybe_action = step.get("uses")
            if maybe_action is None:
                continue
            actions.add(maybe_action)

    return actions


def main(argv: List[str] = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        print(
            colored(
                "Usage: check-latest-actions.py WORKFLOW_YAML [WORKFLOW_YAML]",
                "red",
            ),
            file=sys.stderr,
        )
        return 1

    if not API_TOKEN:
        print(
            colored("ERROR: GITHUB_TOKEN env var is empty. Exit...", "red"),
            file=sys.stderr,
        )
        return 1

    all_actions: Set[str] = set()
    storage: DefaultDict[str, List[Path]] = DefaultDict(list)

    for item in argv:
        path = Path(item)

        maybe_actions = process_workflow_yaml(path)
        if maybe_actions is None:
            print(
                colored(
                    f"ERROR: Unable to process workflow config at {item}. "
                    "Exit...",
                    "red",
                ),
                file=sys.stderr,
            )
            return 1

        all_actions.update(maybe_actions)
        for action in maybe_actions:
            storage[action].append(path)

    with requests.session() as session:
        session.headers["Authorization"] = f"Bearer {API_TOKEN}"
        for item in sorted(all_actions):
            diff = check_latest_version(session, value=item)
            if diff is None:
                continue
            print_diff(diff, storage[diff.raw_action])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
