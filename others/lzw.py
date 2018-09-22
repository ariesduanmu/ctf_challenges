# -*- coding: utf-8 -*-
'''
Lempel–Ziv–Welch Compression
'''
import unittest

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
    print(builder)
    return result

def generate_builder(data):
    builder = {d:ord(d) for d in set(data)}
    n = 0x81
    pre = None
    for d in data:
        if pre is None:
            pre = d
        else:
            p_c = pre+d
            if p_c not in builder:
                builder[p_c] = n
                n += 1
                pre = d
            else:
                pre = p_c
    return {builder[k]:k for k in builder}

def expand(data):
    builder = {}
    result = ""
    n = 0x81
    for i in range(len(data)):
        d = data[i]
        if d == 0x80:
            break
        if d < 0x80:
            result += chr(d)
        else:
            if d in builder:
                result += builder[d]
            else:
                builder = generate_builder(result)
                if d in builder:
                    result += builder[d]
                else:
                    result += builder[data[i-1]] + builder[data[i-1]][0]
    return result

class LZWTest(unittest.TestCase):
    def test_1(self):
        data = "AAAAAAAAAAAAAAAAAA"
        self.assertEqual(expand(compress(data)), data)

    def test_2(self):
        data = "TOBEORNOTTOBE"
        self.assertEqual(expand(compress(data)), data)

    def test_3(self):
        data = "YABBADABBADABBADOO"
        self.assertEqual(expand(compress(data)), data)

    def test_4(self):
        data = "ABABABABABABABABAB"
        self.assertEqual(expand(compress(data)), data)


if __name__ == "__main__":
    unittest.main()