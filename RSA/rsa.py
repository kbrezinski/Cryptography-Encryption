
from typing import Tuple

# Two large primes


def main():

    # selected primes
    p = 11
    q = 17

    # eulers function (totient)
    n = p * q
    phi = (p - 1) * (q - 1)


def egcd(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def gcd(a: int, b: int):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def modinv(a: int, b: int) -> int:
    g, x, _ = egcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b


def coprimes(a: int):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x, phi) != None: pass


if __name__ == '__main__':
    main()



