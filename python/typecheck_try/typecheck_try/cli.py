from pathlib import Path

from semver import VersionInfo

def nextversion(version: VersionInfo) -> VersionInfo:
    return version.bump_minor()

def cli(argv: list[str]) -> int:
    path = Path(argv[0])
    version_str = argv[1]

    version = VersionInfo.parse(version_str)

    next = nextversion(version)

    with path.open(mode="w") as f:
        f.write(str(nextversion))
    return 0
