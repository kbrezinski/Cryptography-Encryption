
from binascii import unhexlify


def brute_force(input, key):
    if len(input) != len(key):
        return "Failed!"

    output = b''
    for b1, b2 in zip(input, key):
        output += bytes([b1 ^ b2])

    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"


data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher = unhexlify(data)

print(f"[-] CIPHER: {cipher}\n")

# First Step
key1 = brute_force(cipher[:7], "crypto{".encode())
print(f"[-] PARTIAL KEY FOUND: {key1}")

# Second Step
key = (key1 + 'y').encode()
key += key * int((len(cipher) - len(key)) / len(key))

key += key[:(len(cipher) - len(key)) % len(key)]
print(key)
print(f"[-] PARTIAL KEY FOUND: {key}")

text = brute_force(cipher, key)
print(f"[*] PLAIN_TEXT: {text}")

#print("[*] FLAG: {}".format([s for s in result.values()]))