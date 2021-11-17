
from Crypto.PublicKey import RSA

'''
NOTES:
key = (m, e=65537, d, p, q, u) where:

n = RSA modulus (p * q)
e = RSA public exponent (must be odd and larger than 1)
d = private exponent (e * d = 1 mod phin)
p, q = both factors of n
u = CRT coefficient (p * u = 1 mod q)
'''

# custom key creation, 32 bits
key = RSA.construct((
    2228434223,  # n
    65537,  # e
    2122969025,  # d
    54449,  # p
    40927  # q
))  # generate public and private keys

# save key to pwd
with open('../RSA/mykey.pem', 'wb') as f:
    f.write(key.export_key('PEM'))

# constants
message = b'Hello from Kenneth Brezinski'
message_hex = message.hex()
print(f"{message_hex = }")

d = int('A863F4B19CD0957470DBC0F1ECC825283D79CCE9831292F029C4AEFEF956BE95CBFBCCE074966F17B877B765EFF54054A1439E5C0963767F297FF95F572EC291', 16)
n = int('B6676AAD44AA71E8F5360A777F8C2C4FBA69AC5A7B36FD5436B03E6F629F02B9B2C5728F2EBD44D36FEFD75F609741E7D5A5FEA8D2D25AFAC80FB3969864C9F3', 16)
e = int('010001', 16)

# determine RSA signature | hex -> base16
certificate = pow(int(message_hex, 16), d, n)
print(f"{hex(certificate) = }")

# validate the signature
validation = pow(certificate, e, n)
print(f"{bytearray.fromhex(hex(validation)[2:]) = }")

# existential forgery attack
s = 0xf  # forged signature
hex_str = bytes.fromhex(hex(pow(s, e, n))[2:])
print(f"{hex_str[2:] = }")

plain_text = ''
for b in hex_str:
    if b < 128:
        plain_text += chr(b)
    else:
        plain_text += '*'

print(f"ASCII x: {plain_text}")




