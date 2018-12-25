# -*- coding: utf-8 -*-
'''
You fill the mug with some nice hot chocolate before leaving, 
and you can refill it along the way by visiting vendors. 
For the sake of simplicity, the capacity (mugSize) is measured in terms of 
how far it'll allow you to travel.

Given destination (the distance from your starting point to the winter coat store), 
mugSize, and vendors, your task is to find the minimum total you'll have to pay 
in order to make it to your destination without ever fully emptying your mug! 
If it's not possible, return -1.
'''
import unittest
import heapq as pq

def stayWarm(destination, mugSize, vendors):
    '''heapq is efficient, it will pop the min one
    '''
    costs = {}
    vendors = [[0,0]] + vendors
    q = [[0,0]]
    result = -1
    while q:
        cost, index = pq.heappop(q)
        if vendors[index][0] + mugSize >= destination:
            c_cost = cost + vendors[index][1]
            result = min(result,c_cost) if ~result else c_cost
            continue
        
        for n in range(index+1,len(vendors)):
            loc = vendors[n][0]
            n_cost = cost + vendors[index][1]
            if loc - vendors[index][0] <= mugSize:
                if n not in costs or n_cost < costs[n]:
                    costs[n] = n_cost
                    pq.heappush(q,[n_cost, n])
            else:
                break
    return result

class TestIceCave(unittest.TestCase):
    def test1(self):
        destination = 40
        mugSize = 15
        vendors = [[10,250], 
                   [13,500], 
                   [25,149], 
                   [26,200]]
        output = 399
        self.assertEqual(stayWarm(destination, mugSize, vendors), output)

    def test2(self):
        destination = 100
        mugSize = 10
        vendors = [[5,219], 
                   [13,41]]
        output = -1
        self.assertEqual(stayWarm(destination, mugSize, vendors), output)

    def test3(self):
        destination = 52
        mugSize = 100
        vendors = []
        output = 0
        self.assertEqual(stayWarm(destination, mugSize, vendors), output)

    def test4(self):
        destination = 317
        mugSize = 16
        vendors = [[2,275], 
                   [23,113], 
                   [33,502], 
                   [56,311], 
                   [58,921], 
                   [65,842], 
                   [76,328], 
                   [80,317], 
                   [102,296], 
                   [105,646], 
                   [109,493], 
                   [133,260], 
                   [147,505], 
                   [167,844], 
                   [168,997], 
                   [187,853], 
                   [189,483], 
                   [201,432], 
                   [222,554], 
                   [241,844], 
                   [262,91], 
                   [284,817], 
                   [293,458], 
                   [305,627]]
        output = -1
        self.assertEqual(stayWarm(destination, mugSize, vendors), output)

    def test5(self):
        destination = 143
        mugSize = 25
        vendors = [[13,805], 
                   [21,485], 
                   [24,894], 
                   [39,889], 
                   [40,130], 
                   [45,452], 
                   [62,943], 
                   [81,847], 
                   [101,625], 
                   [113,872], 
                   [124,109]]
        output = 3139
        self.assertEqual(stayWarm(destination, mugSize, vendors), output)


if __name__ == "__main__":
    unittest.main()