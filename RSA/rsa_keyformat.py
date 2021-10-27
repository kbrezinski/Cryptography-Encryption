import base64

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) # generate public and private keys

'''
key = (m, e=65537, d, p, q, u) where:

n = RSA modulus (p * q)
e = RSA public exponent (must be odd and larger than 1)
d = private exponent (e * d = 1 mod phin)
p, q = both factors of n
u = CRT coefficient (p * u = 1 mod q)
'''
print(key.public_key())