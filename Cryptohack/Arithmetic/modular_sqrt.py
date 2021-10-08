

def tonelli_shanks(a: int, p: int):

    # check if residue
    if not is_residue(a, p):
        return -1




def is_residue(a: int, p: int) -> bool:

    if pow(a, (p - 1) // 2,  p) == 1:
        return True
    else:
        return False


with open("output_modular.txt") as f:
    lines = f.read().splitlines()
    a = int(lines[0])
    p = int(lines[1])


