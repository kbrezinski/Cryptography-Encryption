
"""
Rearranging fermat's little theorem, using math notation...
a^p-1 = 1 mod p
a^p-2 = a^-1 mod p

"""
a = 3
p = 13
print(pow(a, p-2, p))
