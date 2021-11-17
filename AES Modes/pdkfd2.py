
'''
encrypt something with a password using PBKDF2 - password-based key derivation function 2

'''

import hashlib
from Crypto.Cipher import AES

# derive a 16-bit key from the password using one round of HMAC-MD5 with no salt
password = b"password"
key = hashlib.pbkdf2_hmac('md5', password, b"", 1, 16).hex()

# derive a 16-bit key and use that to encrypt some plaintext using AES
text = b'Any nation that does not honor its heroes will not long endure. '

key = hashlib.pbkdf2_hmac('md5', b"apple", b"", 1, 16)
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(text)
print(f"{ciphertext.hex() = }")
print(f"{cipher.decrypt(ciphertext) = }")

# guess a key based on a preset configuration and known key = [0, 1000)
def guess_key():
    for i in range(1000):
        key = hashlib.pbkdf2_hmac('sha1',
                                  i.to_bytes(2, byteorder="big"),
                                  b"aaaabbbb",
                                  1000, 4).hex()

        if key == 'f68923f5':
            print(f"Found key at iteration: {i}")

