# -*- coding: utf-8 -*-
'''
So, given n - the total number of small snowballs and k - 
the number of main snowballs, 
from which a snowman should be constructed, 
you need to find how many small snowballs is needed for each main snowball. 
It's guaranteed that n small snowballs can be distributed among k main snowballs 
in the required way.
'''
from itertools import combinations_with_replacement

def fibonacciSnowman_1(n, k):
    f = [1, 2]
    while f[-1] < n:
        f += [sum(f[-2:])]
    for m in combinations_with_replacement(f, k):
        if sum(m) == n:
            return m

def fibonacciSnowman_2(n, k):
    r = []
    while k:
        x = y = 1
        k -= 1
        while y <= n-k:
            x, y = y, x+y

        n -= x
        r += [x]
    return r

