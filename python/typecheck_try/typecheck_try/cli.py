from pathlib import Path

from semver import Version

def nextversion(version: Version) -> Version:
    return version.dump_minor()

def cli(argv: list[str]) -> int:
    path = Path(argv[0])
    version_str = Path(argv[1])

    version = Version.parse(version_str)

    next = nextversion(version)

    with path.open(mode="w") as f:
        f.write(str(nextversion))
    return 0
