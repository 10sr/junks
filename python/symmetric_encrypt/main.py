#!/usr/bin/env python2

# Not work?
# http://bityard.blogspot.jp/2010/10/symmetric-encryption-with-pycrypto-part.html

import binascii
from Crypto.Cipher import AES


def enc(string, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(string.decode("utf-8")).encode("hex")


def dec(string, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(binascii.unhexlify(string))


if __name__ == "__main__":
    text = "hogehoge"
    key = "hoehoe"

    print(text)

    encrypted = enc(text, key)
    print(encrypted)

    decrypted = dec(encrypted, key)
    print(decrypted)
