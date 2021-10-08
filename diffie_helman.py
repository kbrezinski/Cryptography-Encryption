
key_a = 17
key_b = 44_207

g = 3
n = 57_349

message = "IM THE WINNER AND YOU'RE NOT!"


# encrypt function given key, g, n
def encrypt(key: int, g: int, n: int):
    ans = pow(g, key, n)
    print(f"{key=} {ans=}")
    return ans


def encrypt_message(key: int, text: str):

    cipher = ''
    for i, c in enumerate(range(len(text))):
        cipher += chr(ord(text[i]) ^ key)

    print(f"{cipher=}")
    return cipher


def brute_force(max_len: int, mess: str):
    for i in range(max_len + 1):
        encrypt_message(i, mess)


brute_force(key_b, encrypt_message(key_b, message))


#encrypt(key_a, ans_b, n)
#encrypt(key_b, ans_a, n)

