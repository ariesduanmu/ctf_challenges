# -*- coding: utf-8 -*-
'''
Lempel–Ziv–Welch Compression
'''
def compress(data):
    builder = {d:ord(d) for d in set(data)}
    n = 0x81
    result = []
    pre = None
    for d in data:
        if pre is None:
            pre = d
        else:
            p_c = pre+d
            if p_c not in builder:
                builder[p_c] = n
                n += 1
                result += [builder[pre]]
                pre = d
            else:
                pre = p_c
    result += [builder[pre]]
    result += [0x80]
    print(result)


def expand(data):
    pass





if __name__ == "__main__":
    data = "ABRACADABRABRABRA"
    d = [65, 66, 82, 65, 67, 65, 68, 129, 131, 130, 136, 65, 128]
    # compress(data)
    expand(d)
