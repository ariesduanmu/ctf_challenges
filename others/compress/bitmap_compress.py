# -*- coding: utf-8 -*-
from dumps import binary_dump

def compress(data):
    c = "0"
    l = 0
    d = []
    for i in range(len(data)):
        b = data[i]
        if b == c:
            l += 1
        else:
            c = b
            d += [l]
            l = 1
        if i == len(data) - 1:
            d += [l]
    compressed = "".join("{:08b}".format(i) for i in d)
    print(f"After compress: {len(compressed)} bits")
    return compressed

def expand(data):
    o = ["0","1"]
    c = 0
    expanded = ""
    for i in range(0, len(data), 8):
        l = int(data[i:i+8],2)
        expanded += o[c] * l
        c ^= 1
    print("\n".join(expanded[i:i+16] for i in range(0,len(expanded),16)))
    print(f"{len(expanded)} bits")
    return expanded

if __name__ == "__main__":
    text = "00000000000000000000000000000000001111111100000000000000111111"
    compressed = compress(text)
    expand(compressed)
