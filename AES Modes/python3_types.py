
def int_2_str(i):
    string = str(i)
    print(f"{i = } converted into {string = }")
    return string


def int_2_bytes(i):

    assert isinstance(i, (bytes, int)), "input needs to be bytes or int, you used {}".format(type(i))
    integer = None

    if isinstance(i, bytes):
        integer = i[0]
    else:
        integer = i.to_bytes(1, byteorder="big")

    print(f"{i = } converted into {integer = }")


def str_2_bytes(i):

    assert isinstance(i, (bytes, str)), "input needs to be bytes or str, you used {}".format(type(i))
    byte = None

    if isinstance(i, bytes):
        byte = i.decode('utf-8')
    else:
        byte = bytes(i, 'utf-8')

    print(f"{i = } converted into {byte = }")


int_2_str(2)
int_2_bytes(5)
str_2_bytes('hello!')
















