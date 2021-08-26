

def main():

    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift = 5
    cipher_text = ""

    # restrict to 65 - 122
    for c in text:
        # print(ord(c))
        cipher = ord(c) + shift
        if cipher > 122:
            cipher -= 58
        elif cipher < 65:
            cipher += 58

        print(cipher)
        cipher_text += chr(cipher)

    print(f"{text = }")
    print(f"{cipher_text = }")


if __name__ == '__main__':
    main()

