
from Crypto.Util.number import inverse
import math


def find_factors(n: int) -> int:

    # find the sqrt to find starting point
    tmp = int(math.sqrt(n))

    # if tmp is even, increment by 1 to made it odd
    if tmp % 2 == 0:
        tmp += 1

    for i in range(tmp, 0, -2):
        if n % i == 0:
            print(f'Found divisor at {i=}')
            return i
        else:
            print(f'Tried divisor at {i=}')

    return -1


def main():

    # we are given the public key as (10142789312725007, 5)
    e = 5
    n = 10142789312725007

    # need to find a way to factor such a large number
    p, q = None, None  # p and q are unknown
    p = find_factors(n)
    q = int(n / p)
    phi = (p - 1) * (q - 1)

    # print constants
    print(f"{p=} | {q=} | {n=} | {e=} | {phi=}")

    # determines multiplicative inverse where d * e = 1 mod phi
    d = inverse(e, phi)
    assert d * e % phi == 1, "modulo is not 1"

    # convert message to integer
    text = [ord(c) for c in 'My secret message!']

    # encrypt with public
    cipher = [pow(c, e, n) for c in text]

    # decrypt with multiplicative inverse d
    plaintext = [pow(c, d, n) for c in cipher]
    print(''.join([chr(c) for c in plaintext]))


if __name__ == '__main__':
    main()
