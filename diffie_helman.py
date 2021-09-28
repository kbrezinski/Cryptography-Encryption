
a = 17
b = 13

g = 14
n = 100

a1 = (g ** a) % n
b1 = (g ** b) % n

print(f"a1 = {a1} | b1 = {b1}")

a2 = (b1 ** a) % n
b2 = (a1 ** b) % n

print(f"a2 = {a2} | b2 = {b2}")