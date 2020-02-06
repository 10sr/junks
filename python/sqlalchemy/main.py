#!/usr/bin/env python3

from sqlalchemy import create_engine


def main():
    engine = create_engine('sqlite:///:memory:')
    print(engine)
    return


if __name__ == "__main__":
    main()
