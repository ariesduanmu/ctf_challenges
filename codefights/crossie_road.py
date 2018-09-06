# -*- coding: utf-8 -*-
'''
Over the past week, you have been addicted to the hit game CrossieRoad, 
so much that you want to write an algorithm to beat the game. 
The premise of the game is that you're trying to cross a busy road, 
and you need to find a time when all the lanes are clear.

Details:
* There are multiple lanes of traffic, each with a continuous stream of cars, 
represented by the array lanes
* Each lane's cars follow a pattern where every car in the lane has the same 
length and the distance between each car is the same
* Some lanes will have a delay before the first car crosses in front of you
* All cars (in all lanes) are moving in the same direction, at the same speed
* Each element in lanes is of the following format:
[length of car, interval between cars, delay before first car passes]

Given the array lanes, your task is to return the time at which all lanes will be clear (or -1 if they will never all be clear at the same time).
'''
import unittest

def crossieRoad_bruteforce(lanes):
    '''
    brute force
    my solution was close to it, but I spend too much time in lots (meaningless) if/else in while loop 
    '''
    if len(lanes) == 0:
        return 1
    i = 0
    while i < 415000:
        for x,y,z in lanes:
            if (i-z)%(x+y)<x:
                break;
        else:
            return i + 1
        i += 1 
    return -1

def crossieRoad(lanes):
    # array of safe positions (cyclic, 0 based)
    safe = [0]
    # n = current period of highway
    n = 1
    for length, interval, delay in lanes:
        new_safe = []
        size = length + interval
        k = 0
        while n*k % size or k == 0:
            for x in safe:
                y = n*k + x
                z = y % size
                if z < delay or z >= delay + length:
                    new_safe.append(y)
            k += 1
        n *= k
        safe = new_safe
    return safe[0] + 1 if safe else -1


class CrossieRoadTest(unittest.TestCase):
    def test_1(self):
        lanes = [[1,1,0], 
                 [2,1,0], 
                 [2,2,1]]
        output = 12
        self.assertEqual(crossieRoad(lanes), output)

    def test_2(self):
        lanes = []
        output = 1
        self.assertEqual(crossieRoad(lanes), output)

    def test_3(self):
        lanes = [[1,1,0]]
        output = 2
        self.assertEqual(crossieRoad(lanes), output)

    def test_4(self):
        lanes = [[1,0,0]]
        output = -1
        self.assertEqual(crossieRoad(lanes), output)

    def test_5(self):
        lanes = [[9,10,1], 
                 [3,13,0], 
                 [9,14,7], 
                 [9,9,6], 
                 [9,5,3], 
                 [6,14,5], 
                 [1,12,7], 
                 [2,8,4], 
                 [8,8,3], 
                 [4,10,0]]
        output = 812
        self.assertEqual(crossieRoad(lanes), output)

    def test_6(self):
        lanes = [[7,9,0], 
                 [7,7,3], 
                 [4,9,6]]
        output = 11
        self.assertEqual(crossieRoad(lanes), output)

    def test_7(self):
        lanes = [[2,2,2], 
                 [2,3,2], 
                 [1,9,2], 
                 [3,7,0], 
                 [4,7,1], 
                 [1,3,2], 
                 [4,5,0], 
                 [3,2,0]]
        output = 45
        self.assertEqual(crossieRoad(lanes), output)

    def test_8(self):
        lanes = [[1,2,0], 
                 [2,1,1]]
        output = -1
        self.assertEqual(crossieRoad(lanes), output)

    def test_9(self):
        lanes = [[6,6,0], 
                 [5,3,1], 
                 [3,6,0], 
                 [2,5,0], 
                 [5,3,1], 
                 [8,3,1], 
                 [7,5,0], 
                 [3,7,0], 
                 [5,3,1], 
                 [4,7,0], 
                 [2,4,1], 
                 [9,3,0], 
                 [8,6,0], 
                 [1,4,1], 
                 [6,7,1], 
                 [4,6,0], 
                 [5,3,1], 
                 [8,4,1], 
                 [7,5,1], 
                 [4,7,1], 
                 [8,4,0], 
                 [4,8,1], 
                 [1,4,1], 
                 [8,4,1], 
                 [4,5,0], 
                 [9,8,1], 
                 [2,9,1], 
                 [5,9,0], 
                 [4,3,1], 
                 [7,3,0], 
                 [8,7,0], 
                 [7,3,1], 
                 [4,7,1], 
                 [5,6,1], 
                 [6,6,0], 
                 [6,6,1], 
                 [8,4,1], 
                 [9,8,1], 
                 [2,7,0], 
                 [1,4,0], 
                 [4,4,0], 
                 [7,3,1], 
                 [9,6,1], 
                 [8,4,0], 
                 [3,5,0], 
                 [6,6,0], 
                 [3,3,0], 
                 [4,9,1], 
                 [6,4,1], 
                 [7,3,1]]
        output = 30239
        self.assertEqual(crossieRoad(lanes), output)

    def test_10(self):
        lanes = [[4,4,5], 
                 [1,7,2], 
                 [2,5,0], 
                 [1,7,5], 
                 [3,5,1], 
                 [4,9,2]]
        output = 13
        self.assertEqual(crossieRoad(lanes), output)

if __name__ == "__main__":
    unittest.main()