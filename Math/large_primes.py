
"""
Implement Fermat primality test and find large primes
"""

from random import randint
import math

# Fermat's little theorem states if p is prime and a is not divisible by p, then:
# a ^ (p-1) = 1 mod p


def fermat(p: int):

    #print(f"Testing potential prime: {p}")
    flag = False

    for _ in range(5):  # try 5 random guesses
        a = randint(2, p-2)
        if pow(a, p-1, p) == 1:
            print(f"PASSES - {a}")
            flag = True
        else:
            # print(f"FAIL - {a}")
            break

    return flag
    # print()


# test the fermat function
def test_fermat():
    for i in (11, 13, 100, 121):
        fermat(i)


# expected density of primes is 1 / ln(N) where N is the number in the set
def test_density():
    for N in (300, 1000):  # 1024-bit = 300, 3000-bit = 1000 digits
        print(f"Prime density for 10^{N} is : {1 / math.log(10**N) * 100:.4f}%")


# find a larger prime than 10^300
for i in range(10**300, 10**301):
    if fermat(i):
        print(f"Found prime at {i}")
        break
