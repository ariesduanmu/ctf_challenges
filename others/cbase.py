# -*- coding: utf-8 -*-
import string

base = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
d_base = {i:base[i] for i in range(len(base))}
r_base = {base[i]:i for i in range(len(base))}

def encode(original):
    bins = "".join("{:08b}".format(ord(s)) for s in original)
    if len(bins) % 6 > 0:
        bins += "0" * (6 - (len(bins) % 6))
    encoded = ""
    for i in range(0,len(bins), 6):
        encoded += d_base[int(bins[i:i+6],2)]
    if len(encoded) % 4 == 0:
        return encoded
    return encoded + "=" * (4 - (len(encoded) % 4))

def decode(encoded):
    encoded = encoded.replace("=","")
    bins = "".join("{:06b}".format(r_base[e]) for e in encoded)
    if len(bins) % 8 > 0:
        bins = bins[:(len(bins) % 8) * -1]
    return "".join(chr(int(bins[i:i+8],2)) for i in range(0, len(bins), 8))

if __name__ == "__main__":
    print(decode("QkM="))
