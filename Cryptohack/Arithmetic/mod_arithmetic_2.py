
"""
Fermat's little theorem

is p is prime, for every integer a:
    pow(a, p) = a mod p
if p is prime and a is an integer coprime with p,
    pow(a, p - 1) = 1 mod p


"""

from math import gcd
print(gcd(273246787654, 65537))

def modulo(a, b, n):
    return (a ** b) % n

print(modulo(3, 17, 17))
print(modulo(5, 17, 17))
print(modulo(7, 16, 17))

# if p is the exponent and operator, then the base is returned
# otherwise,