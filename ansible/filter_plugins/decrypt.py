#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
from cryptography.fernet import Fernet
import hashlib


def _enc(data, key):
    key_32 = base64.urlsafe_b64encode(hashlib.sha512(key).digest()[:32])
    f = Fernet(key_32)
    return f.encrypt(data)


def _dec(b, key):
    key_32 = base64.urlsafe_b64encode(hashlib.sha512(key).digest()[:32])
    f = Fernet(key_32)
    return f.decrypt(b)


def decrypt_filter(data, key):
    return _dec(data.encode("utf-8"), key.encode("utf-8")).decode("utf-8")


class FilterModule (object):
    def filters(self):
        return {
            "decrypt": decrypt_filter
        }


if __name__ == "__main__":
    import sys
    print(_enc(sys.argv[1].encode("utf-8"), sys.argv[2]))
