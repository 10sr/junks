import sys

from .cli import cli as cli

if __name__ == "__main__":
    raise SystemExit(cli(sys.argv[1:]))
