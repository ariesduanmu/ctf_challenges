# -*- coding: utf-8 -*-
from quadtree import QuadTree 
from slowfrisbees import frisbees as sfrisbees
import unittest

def frisbee_tree(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    x_min, x_max, y_min, y_max = min(x), max(x), min(y), max(y)
    center_x, center_y = (x_min + x_max) / 2, (y_min + y_max) / 2
    width, height = (x_max - x_min) / 2, (y_max - y_min) / 2
    return QuadTree((center_x, center_y, width, height), 4)

def frisbees(friends, number_of_passes, player):
    ft = frisbee_tree(friends)
    for i in range(len(friends)):
        ft.insert([i]+friends[i])
    frisbee_held = {i: 0 for i in range(len(friends))}
    throwable_friends = [ft.throwable([i]+friends[i]) for i in range(len(friends))]
    
    for _ in range(number_of_passes):
        frisbee_held[player] += 1
        player = min(throwable_friends[player], key=frisbee_held.get)
    return player


class FrisbeesTest(unittest.TestCase):
    def test_1(self):
        friends = [[152,213,276], 
                  [274,259,151], 
                  [40,57,130], 
                  [203,87,189], 
                  [43,182,163]]
        numberOfPasses = 19
        startingPlayer = 4
        output = 4
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer), output)
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer),
        #                  sfrisbees(friends, numberOfPasses, startingPlayer))
        self.assertEqual(sfrisbees(friends, numberOfPasses, startingPlayer), output)

    def test_2(self):
        friends = [[119,356,361], 
                   [1,106,238], 
                   [222,101,346], 
                   [6,375,360], 
                   [62,369,97], 
                   [356,44,150], 
                   [371,209,403], 
                   [225,29,295], 
                   [49,8,429], 
                   [334,175,427]]
        numberOfPasses = 499
        startingPlayer = 6
        output = 5
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer), output)
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer),
        #                  sfrisbees(friends, numberOfPasses, startingPlayer))
        self.assertEqual(sfrisbees(friends, numberOfPasses, startingPlayer), output)

    def test_3(self):
        friends = [[55,281,236], 
                   [134,281,394], 
                   [356,215,326], 
                   [102,53,411], 
                   [71,278,258], 
                   [111,187,149], 
                   [335,5,238], 
                   [164,22,434], 
                   [304,279,144], 
                   [197,195,320]]
        numberOfPasses = 81
        startingPlayer = 2
        output = 9
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer), output)
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer),
        #                  sfrisbees(friends, numberOfPasses, startingPlayer))
        self.assertEqual(sfrisbees(friends, numberOfPasses, startingPlayer), output)

    def test_4(self):
        friends = [[303,176,296], 
                   [78,79,296], 
                   [53,97,384], 
                   [98,40,225], 
                   [204,33,210], 
                   [288,162,438], 
                   [39,215,149], 
                   [318,227,95]]
        numberOfPasses = 290
        startingPlayer = 3
        output = 7
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer), output)
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer),
        #                  sfrisbees(friends, numberOfPasses, startingPlayer))
        self.assertEqual(sfrisbees(friends, numberOfPasses, startingPlayer), output)

    def test_5(self):
        friends = [[152,246,136], 
                   [380,375,301], 
                   [213,147,296], 
                   [158,291,112], 
                   [344,25,219], 
                   [42,148,354], 
                   [4,41,218], 
                   [247,323,333], 
                   [379,54,334], 
                   [19,146,195], 
                   [375,262,223], 
                   [66,2,226], 
                   [357,347,303], 
                   [46,56,328], 
                   [324,397,422], 
                   [255,340,191], 
                   [331,82,216], 
                   [37,139,405], 
                   [79,59,127], 
                   [315,283,239]]
        numberOfPasses = 203
        startingPlayer = 9
        output = 3
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer), output)
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer),
        #                  sfrisbees(friends, numberOfPasses, startingPlayer))
        self.assertEqual(sfrisbees(friends, numberOfPasses, startingPlayer), output)

    def test_6(self):
        friends = [[17,4,432], 
                   [298,350,228], 
                   [173,266,394], 
                   [116,44,214]]
        numberOfPasses = 710
        startingPlayer = 0
        output = 3
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer), output)
        # self.assertEqual(frisbees(friends, numberOfPasses, startingPlayer),
        #                  sfrisbees(friends, numberOfPasses, startingPlayer))
        self.assertEqual(sfrisbees(friends, numberOfPasses, startingPlayer), output)

if __name__ == "__main__":
    unittest.main()




