#!/usr/bin/env python3

from pushbullet import Pushbullet


def main():
    with open("token.secret") as f:
        token = f.read().strip()
    print(token)

    pb = Pushbullet(token)
    # print(pb.push_note("this is title", "hoehoe"))
    for d in pb.devices:
        print(d.nickname)
        print(d.device_iden)

    myiphone = pb.get_device("yuk-iPhoneSE-g")
    print(myiphone)
    print(myiphone.push_note("title", "body"))

    return


main()
