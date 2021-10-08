
from Crypto.Cipher import AES

key = b'0000111122223333'
cipher = AES.new(key, AES.MODE_ECB)

a = b'Hello from AES!!'
ciphertext = cipher.encrypt(a)

print(ciphertext.hex())

d = cipher.decrypt(ciphertext)
print(d)