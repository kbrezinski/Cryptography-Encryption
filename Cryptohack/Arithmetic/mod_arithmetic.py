
# congruent modulu if a == b mod m

def cong_mod_solver(a, n):
    b = 0
    while (a - b) % n != 0:
        b += 1
    return a, b, n


print(cong_mod_solver(11, 6))
print(cong_mod_solver(8146798528947, 17))