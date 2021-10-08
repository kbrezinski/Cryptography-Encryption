
"""
Quadratic Residues
-we say x is a quadratic residue if there exists an a such that:
    a**2 = x mod p

"""


def is_residue(x: int, p: int) -> int:

    # there exists an a where: a ^ 2 = x mod p
    for a in range(p):
        if (a * a) % p == x:
            return a
    return -1


p = 29
ints = [14, 6, 11]

for i in ints:
    print(f"{i} has residue: {is_residue(i, 29)}")
