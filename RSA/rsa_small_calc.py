
from typing import Tuple, List


def choose_primes(test=True) -> Tuple[int, int]:
    if test:
        return 7, 23


def choose_e(test=True) -> int:
    if test:
        return 5


def find_d(e: int, phi: int, test=True) -> int:
    if test:
        return 53

    d = 1
    while (d * e) % phi != 1:
        d += 1
    print(f'{d=}')
    return d


def encrypt(message: str, e: int, n: int):
    if isinstance(message, List):
        cipher = [pow(c, e, n) for c in message]
    else:
        cipher = [pow(ord(c), e, n) for c in message]

    print(cipher)
    return cipher


def decrypt(cipher: List[int], d: int, n: int):

    plaintext = ''.join([chr(pow(c, d, n)) for c in cipher])
    print(plaintext)
    return plaintext


def main():

    # choose primes, determine quotient and phi
    p, q = 13, 41  # choose_primes()
    n = p * q
    phi = (p - 1) * (q - 1)

    # print constants
    print(f"{p=} | {q=} | {n=} | {phi=}")

    # choose public exponent between 1 and phi - 1. Cannot share divisors with phi.
    e = 7  # choose_e()
    d = find_d(e, phi, test=False)

    # preamble
    # message = 'Hi!'
    # cipher = encrypt(message, e, n)
    cipher = [460, 364, 144, 153, 501, 402, 19, 311, 501, 280, 501, 80, 153, 382, 296, 153, 311]
    text = decrypt(cipher, d, n)


if __name__ == '__main__':
    main()
