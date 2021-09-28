
def key_decrypt(key, cipher):

    key = bytes.fromhex(key)
    cipher = bytes.fromhex(cipher)

    return bytes([k ^ c for c, k in zip(key, cipher)]).hex()

# constants
k1  = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
k12 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
k23 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
txt = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

k2 = key_decrypt(k1, k12)
k3 = key_decrypt(k2, k23)

flag = key_decrypt(key_decrypt(key_decrypt(txt, k1), k2), k3)
print(bytes.fromhex(flag).decode("ASCII"))