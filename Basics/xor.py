

def main():

    text = "HELLO"
    key = "FNSDOJNGFOSDNFGOJNSOGFOPGNOPGFSP"

    encrypt = [chr(ord(a) ^ ord(b)) for a, b in zip(text, key)]

    print(encrypt)
    print([bytes.fromhex(h[2:]).decode("ASCII") for h in encrypt])


if __name__ == '__main__':
    main()

