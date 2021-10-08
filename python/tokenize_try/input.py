a = "abc" "def"
g = ["eee",
     "fff"
     "ggg"]

e = b"efe" b"hoehoe"

# e = b"ee" "hoehoe"


def fun1(arg1: int):
    list = ["1",
            "2",
            "hoehoe"
            ]
    for e in list:
        if len(e) > 1:
            print(f"{arg1} {e}")
    return


fun1(4)
