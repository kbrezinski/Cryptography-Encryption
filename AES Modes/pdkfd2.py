
'''
encrypt something with a password using PBKDF2 - password-based key derivation function 2

'''

import hashlib

# derive a 16-bit key from the password using one round of HMAC-MD5 with no salt
password = b"password"
key = hashlib.pbkdf2_hmac('md5', password, b"", 1, 16).hex()

print(key)