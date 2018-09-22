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
    return result

def expand(data):
    builder = {i:chr(i) for i in range(33,127)}
    result = ""
    n = 0x81
    val = builder[data[0]]
    i = 1
    while i < len(data):
        result += val
        if data[i] == 0x80:
            break
        if data[i] in builder:
            s = builder[data[i]]
        if n == data[i]:
            s = val + val[0]

        builder[n] = val + s[0]
        n += 1
        i += 1
        val = s
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