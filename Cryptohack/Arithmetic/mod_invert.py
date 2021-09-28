
from typing import Tuple


# Extended Euclids/Euclidean Algorithm
def egcd(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    else:
        g, u, v = egcd(b % a, a)
        return g, u - (b // a) * v, v


# Simple Euclidean Algorithm
def gcd(a: int, b: int) -> int:

    # Remainder becomes the new factor
    if a == 0:
        return b
    print(f"b % a: {b%a} | new b: {a}")
    return gcd(b % a, a)


# Euler's Test
def is_prime(n: int, b: int) -> bool:

    # Fermat's little theorem test
    if not pow(b, n-1, n) == 1:
        return False

    r = n - 1
    while r % 2 == 0:
        r //= 2

    c = pow(b, r, n)
    if c == 1: # remainder is 1
        return True

    while True:
        if c == 1: return False
        if c == n - 1: return True
        c = pow(c, 2, n)











#print(gcd(12345678, 87654321))

# pow(b,e,n) computes b^e(mod n); if 1 then n is prime
print(pow(2, 100, 101))
