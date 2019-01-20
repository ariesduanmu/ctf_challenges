# -*- coding: utf-8 -*-
from .bintree import Bin_Tree

def firstFit(weights, capacity, print_box=False):
    n = len(weights)
    res = 0
    bin_rem = [capacity for _ in range(n)]
    boxes = [[] for _ in range(n)]
    for i in range(n):
        for j in range(res):
            if bin_rem[j] >= weights[i]:
                bin_rem[j] -= weights[i]
                boxes[j] += [weights[i]]
                break
        else:
            bin_rem[res] -= weights[i]
            boxes[res] += [weights[i]]
            res += 1
            
        if print_box: 
            print(boxes)
    return res

def firstFit_Tree(weights, capacity):
    pass

