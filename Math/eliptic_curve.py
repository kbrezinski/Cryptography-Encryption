
import math


def secp256k1(x, a, b, c):
    return math.sqrt(x**3 + (a * x**2) + (b * x) + 7)

print(secp256k1())

