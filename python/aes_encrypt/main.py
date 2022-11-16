#!/usr/bin/env python3

from Crypto.Cipher import AES, ARC4, DES


def encrypt(key: bytes, data: bytes) -> (bytes, bytes):
    cipher = AES.new(key, AES.MODE_CFB)
    ciphertext = cipher.encrypt(data)
    return (ciphertext, cipher.iv)


key1 = b"key1" * 4
data1 = b"data1"

encrypted, iv = encrypt(key1, data1)
print(repr(encrypted))


def decrypt(key: bytes, data: bytes, iv=None):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    dec = cipher.decrypt(data)
    return dec

print(decrypt(key1, encrypted))
print(decrypt(key1, encrypted, iv))


def encrypt_twice(key: bytes, data1: bytes, data2: bytes) -> dict[str, bytes]:
    cipher = AES.new(key, AES.MODE_CFB)
    ciphertext1 = cipher.encrypt(data1)
    ciphertext2 = cipher.encrypt(data2)
    return {
        "data1": ciphertext1,
        "data2": ciphertext2,
        "iv": cipher.iv,
    }

key2 = b"key2" * 4
data2_1 = b"data2-1"
data2_2 = b"data2-2"


result2 = encrypt_twice(key2, data2_1, data2_2)
print(result2)

print(decrypt(key2, result2["data2"], result2["iv"]))
print(decrypt(key2, result2["data1"], result2["iv"]))
