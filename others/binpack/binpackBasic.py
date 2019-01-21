# -*- coding: utf-8 -*-
def nextFit(weights, capacity, print_box=False):
    n = len(weights)
    res = 0
    bin_rem = capacity
    boxes = [[] for _ in range(n)]
    for i in range(len(weights)):
        if weights[i] > bin_rem:
            res += 1
            bin_rem = capacity - weights[i]
        else:
            bin_rem -= weights[i]
        boxes[res] += [weights[i]]
        
        if print_box: 
            print(boxes)

    return res+1

'''
First Fit can be implemented in O(n Log n) time using 
Self-Balancing Binary Search Trees.
'''
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

'''
Best Fit can also be implemented in O(n Log n) time using 
Self-Balancing Binary Search Trees.
'''
def bestFit(weights, capacity, print_box=False):
    n = len(weights)
    res = 0
    bin_rem = [capacity for _ in range(n)]
    boxes = [[] for _ in range(n)]
    for i in range(n):
        m = capacity + 1
        bi = 0
        for j in range(res):
            if bin_rem[j] >= weights[i] and bin_rem[j] - weights[i] < m:
                bi = j
                m = bin_rem[j] - weights[i]
        if m == capacity + 1:
            bin_rem[res] -= weights[i]
            boxes[res] += [weights[i]]
            res += 1
        else:
            bin_rem[bi] -= weights[i]
            boxes[bi] += [weights[i]]
        if print_box: 
            print(boxes)
    return res 

def firstFitDec(weights, capacity, print_box=False):
    weights = sorted(weights, reverse=True)
    return firstFit(weights, capacity, print_box)

if __name__ == "__main__":

    weights = [[2, 5, 4, 7, 1, 3, 8], [4, 8, 1, 4, 2, 1], [9, 8, 2, 2, 5, 4]]
    capacity = 10
    for weight in weights:
        print(nextFit(weight, capacity))
        print(firstFit(weight, capacity))
        print(bestFit(weight, capacity))
        print(firstFitDec(weight, capacity))
        print("")

