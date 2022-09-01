#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.number import inverse
from Crypto.Util.Padding import pad
from os import urandom

SIZE = 1024

key = RSA.generate(SIZE)
cipher = PKCS1_OAEP.new(key)
master_key = urandom(16)
master_cipher = AES.new(master_key, AES.MODE_ECB)

with open('safe', 'rb') as f:
    plan = pad(f.read(), 16)
with open('safe.lock', 'wb') as f:
    f.write(master_cipher.encrypt(plan))

cf = inverse(key.p, key.q)
hint = key.p & int.from_bytes(b'???', byteorder='big')

print(hex(key.n))
print(hex(cf))
print(hex(hint))

print(cipher.encrypt(master_key).hex())