# -*- coding: utf-8 -*-
import unittest
from cProfile import Profile
from pstats import Stats

'''
Brute Force solution(get TLE)
'''

'''
d = {}
def primeNumberNim(pileSize, maxRemoval):
    global d
    d = {}
    options = [o for o in primes(maxRemoval) if o <= pileSize]
    s = []
    for o in options:
        if win(pileSize-o, options, False):
            s += [o]
    return s

def win(pileSize, options, me):
    global d
    k = f"{pileSize},{me}"
    if k in d:
        return d[k]
    if pileSize == 0 or pileSize == 1:
        return 1 ^ me
    options = [o for o in options if o <= pileSize]
    r = win(pileSize-options[0], options, not me)
    for option in options[1:]:
        s = win(pileSize-option, options, not me)
        if (s < r) != me:
            r = s
    d[k] = r
    return r

def primes(maxRemoval):
    p = [0 for _ in range(maxRemoval+1)]
    p[2] = 1
    p[3] = 1
    for i in range(5, maxRemoval+1, 2):
        j = 2
        while j*j <= i:
            if p[j] == 1 and i % j == 0:
                break
            j += 1
        else:
            p[i] = 1
    return [i for i in range(maxRemoval+1) if p[i] == 1]

'''

def primeNumberNim(pileSize, maxRemoval):
    # build list of primes with Sieve of Eratosthenes
    l = [1]
    M = l * maxRemoval + l
    primes = []
    q = 2
    for q in range(2,maxRemoval+1):
        if M[q]:
            M[q*2::q] = [0] * ((maxRemoval-q)//q)
            primes.append(q)

    # DP to solve
    D = l * (pileSize + maxRemoval)
    for n in range(pileSize):
        if D[n]:
            # if n is a win, set all the removals above it to lose
            for p in primes:
                D[n+p] = 0
    return [p for p in primes if D[pileSize-p]]

class NimGameTest(unittest.TestCase):
    def test_1(self):
        pileSize = 10
        maxRemoval = 9
        output = []
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

    def test_3(self):
        pileSize = 8
        maxRemoval = 7
        output = [7]
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

    def test_4(self):
        pileSize = 13
        maxRemoval = 13
        output = [3, 13]
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

    def test_5(self):
        pileSize = 42
        maxRemoval = 41
        output = [7, 17, 41]
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

    def test_6(self):
        pileSize = 752
        maxRemoval = 11
        output = [5]
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

    def test_7(self):
        pileSize = 161
        maxRemoval = 48
        output = [2]
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

    def test_8(self):
        pileSize = 856
        maxRemoval = 13
        output = []
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

    def test_9(self):
        pileSize = 64804
        maxRemoval = 279
        output = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113, 137, 149, 157, 173, 181, 193, 197, 229, 233, 241, 257, 269, 277]
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

    def test_10(self):
        pileSize = 55190
        maxRemoval = 587
        output = [3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, 107, 127, 131, 139, 151, 163, 167, 179, 191, 199, 211, 223, 227, 239, 251, 263, 271, 283, 307, 311, 331, 347, 359, 367, 379, 383, 419, 431, 439, 443, 463, 467, 479, 487, 491, 499, 503, 523, 547, 563, 571, 587]
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

    def test_11(self):
        pileSize = 47461
        maxRemoval = 255
        output = []
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

    def test_12(self):
        pileSize = 51343
        maxRemoval = 854
        output = [2]
        self.assertEqual(primeNumberNim(pileSize, maxRemoval), output)

def profile_test():
    profiler = Profile()
    profiler.runcall(primeNumberNim, 42, 41)
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()

if __name__ == "__main__":
    unittest.main()