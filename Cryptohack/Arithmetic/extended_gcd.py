
def ext_gcd(p, q):

    if p == 0:
        return q, 0, 1
    else:
        # gcd, s_i, t_i
        gcd, u, v = ext_gcd(q % p, p)
        return gcd, v - (q // p) * u, u


p = 240
q = 46

gcd, u, v = ext_gcd(p, q)

print("[+] GCD: {}".format(gcd))
print("[+] u,v: {},{}".format(u,v))
print(f"\n[*] FLAG: crypto{{{u},{v}}}")