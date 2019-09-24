#!/usr/bin/env python3

import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def gen_key(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
    return key

print(gen_key(b"password", b"salt"))
print(gen_key(b"password", b"salt_"))

msg = b"target_message"

from cryptography.fernet import Fernet

def e(key: bytes, msg: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(msg)

def d(key: bytes, msg: bytes) -> bytes:
    f = Fernet(key)
    return f.decrypt(msg)

encrypted = e(gen_key(b"password", b"salt"), msg)
decrypted = d(gen_key(b"password", b"salt"), encrypted)

print(encrypted)
print(decrypted)

# Fail!
decrypted_2 = d(gen_key(b"password", b"salt_"), encrypted)
print(decrypted_2)
