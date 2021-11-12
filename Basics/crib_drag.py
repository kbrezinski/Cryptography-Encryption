
# two cipher texts
ciph1 = bytes.fromhex('1a0d134503550e0a1d4542071f56')
ciph2 = bytes.fromhex('0d0710071d19490d0e5607004f00074e47')

key = 'The '


def decypher(key, c1, c2):

    # create the empty decypher texts
    d1, d2 = '', ''

    # loop through extra key
    for i, ki in enumerate(key):
        d1 += chr(c1[i] ^ ord(ki))
        d2 += chr(c2[i] ^ ord(ki))

    print("Key: {}".format(key) + '.' * (len(c2) - len(key)))
    print("Msg1: {}".format(d1))
    print("Msg2: {}\n".format(d2))


while True:

    n = input("Enter next guess for key, or 'back' to go back 1 char or 'quit' to break: ")

    if n == 'quit':
        break
    elif n == 'back':
        key = key[:-1]
        print("Reset the last char")
        print("Key: {}".format(key) + '.' * (len(ciph2) - len(key)))
    else:
        key += n
        decypher(key, ciph1, ciph2)









