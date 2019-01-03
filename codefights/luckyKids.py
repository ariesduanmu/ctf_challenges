# -*- coding: utf-8 -*-
'''
Given an array of numbers behaviors, 
each number representing how good a child has behaved in the last year, 
determine how many children will get gifts from santa. 
A child gets a gift if he/she has behaved better than at least half of 
his/her older siblings. The array is sorted by the age of the children.
'''

import bisect
def luckyKids(behaviors):
    s = []
    r = 1
    for b in reversed(behaviors):
        bisect.insort(s, b)
        if len(s) > 1 and bisect.bisect_left(s,b) / (len(s)-1) >= 0.5:
            r += 1
    return r