
from decimal import *
getcontext().prec = 200


# use decimal precision to get precision needed for large numbers
def test_decimal():
    a = 10**100 + 1
    b = a * a
    print(Decimal(b).sqrt())


# p and q are companion primes, so test around the square root
def find_p_and_q(n=10000000000000000016800000000000000005031):
    p0 = int(Decimal(n).sqrt())
    p0 = p0 if p0 % 2 != 0 else p0 + 1  # check if even, if so add 1

    for p in range(p0, p0-10000000, -2):
        if n % p == 0:  # n is factored by p
            print(f"Found {p=} \n and {n // p =}")
            assert n - (p * (n / p)) == 0, "ERROR"
            break


n = 2457319490775870034107936327697724401721210936487723795115696610653082228345978452724879092419462602801287921034412592451829320597304383170626854710604026609207557310932504074259543909051122202199219
find_p_and_q(n)
