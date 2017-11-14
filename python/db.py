#!/usr/bin/env python3

import dbm


def main():
    with dbm.open("a.db", "c") as db:
        db["hoe"] = "fue"
        db["hie"] = "hae"

    with dbm.open("a.db") as db:
        print(db.keys())

    return

if __name__ == "__main__":
    main()
