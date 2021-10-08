"""
Legendre's Symbol
 - a / p = a ^ [(p - 1) / 2] mod p

  1. a / p = 1 if a is a quadratic residue and a /= 0 mod p
  2. a / p = -1 if a is a quadratic non-residue mod p
  3. a / p = 0 if a = 0 mod p
"""

from math import sqrt

def is_residue(a: int, p: int):

    """
    a ^ (p - 1) / 2 = x_o ^ (p - 1) / 2
    therefore:
        x_o ^ (p - 1) = 1 (mod p)

    """
    symbol = pow(a, (p - 1) // 2,  p)

    if symbol == 1:
        return pow(a, (p + 1) // 4, p)


# Read from .txt and save as p and ints
with open("output_legendre.txt", 'r') as f:
    lines = f.read().splitlines()
    p = int(lines[0])
    ints = []
    for line in lines[1:]:
        ints.append(int(line))


for i, a in enumerate(ints):
    print(f"Integer: {i} | {is_residue(a, p)}")