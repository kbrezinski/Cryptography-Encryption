
def gcd(a, b):
    while b != 0:
        b, a = (a % b, b)

    return a


a = 66528
b = 52920

print(gcd(a, b))