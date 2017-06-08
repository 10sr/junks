# -*- coding: utf-8 -*-

from ansible import errors
from gnupg import GPG
# import hashlib
# from Crypto.Cipher import AES

# def dec(data, key):
#     secret_key = hashlib.sha256(key.encode("utf-8")).digest()

def dec(data, key):
    gpg = GPG()
    return gpg.decrypt()


def enc(data, key):
    return

# def enc(data, key):
#     aes = _AESCipher(key)
#     return aes.encrypt(data)


class FilterModule(object):
    def filters(self):
        return {
            "dec": dec
        }
