
from Crypto.Cipher import AES

key = b"aaaabbbbccccdddd"
iv = b"1111222233334444"

def decr(ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return ispkcs7(cipher.decrypt(ciphertext))


# Checks to see if proper padding exists according to PKCS#7
def ispkcs7(plaintext):

    l = len(plaintext)
    c = plaintext[l - 1]

    # Final padding has to have a number between 1 and f
    if (c > 16) or (c < 1):
        return "PADDING ERROR"

    # Checks to see is pkcs#7 compliant
    if plaintext[l - c:] != bytes([c]) * c:
        return "PADDING ERROR"

    return plaintext


def encr(plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pkcs7(plaintext))
    return ciphertext


def pkcs7(plaintext):
    padbytes = 16 - len(plaintext) % 16  # look at number of bytes that is short of 16
    pad = padbytes * bytes([padbytes])   # add the proper multiple, i.e. 01, 0202, 030303
    return plaintext + pad               # add pad bytes onto the end


# Encrypt message
a = b"This sentence clearly says I'M A LOSER."
original = encr(a)
print(f'[*] Encrypted message: {original.hex()}')


prefix = original[0:16] + b"AAAABBBBCCCCDDD"
valid_padding_text = []


for j in range(1, 17):

    # print(f"Starting byte iteration: {j}")
    print([val ^ j for val in reversed(valid_padding_text)])
    for i in range(256):

        mod = prefix + bytes([i] + [val ^ j for val in reversed(valid_padding_text)]) + original[32:]
        if decr(mod) != "PADDING ERROR":
            print(i, "is correctly padded")
            valid_padding_text.append(i ^ j)
            prefix = prefix[:-1]
            break
