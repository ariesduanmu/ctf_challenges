# -*- coding: utf-8 -*-
import unittest

def iceCave(area, direction):
    n, m = len(area), len(area[0])
    goal = [[i,j] for j in range(len(area[0])) \
                  for i in range(len(area)) \
                  if area[i][j] == "G"][0]

    directions = {"N":(0,1), "S":(0,-1), "W":(1,0), "E":(-1,0)}
    rev_directions = {(0,1):"N", (0,-1):"S", (1,0):"W", (-1,0):"E"}
    start_points = { "N":[[i,0] for i in range(m) if area[i][0] != "O"], 
                     "S":[[i,n] for i in range(m) if area[i][n] != "O"], 
                     "W":[[0,i] for i in range(n) if area[0][i] != "O"], 
                     "E":[[m,i] for i in range(n) if area[m][i] != "O"]}
    starts = start_points[direction]
    start_direction = directions[direction]
    paths = [start2goal(start, goal, area, start_direction) \
             for start in starts \
             if start2goal(start, goal, area, start_direction) is not None]
    if len(paths) == 0:
        return "impossible"
    path = min(paths, key=lambda x: len(x))
    return "".join(rev_directions[p] for p in path)

def start2goal(position, goal, area, direction):
    directions = ((0,1),(0,-1),(1,0),(-1,0))
    passed = [f"{position[0]},{position[1]}"]
    found = False
    step = [direction]
    while position != goal and len(passed) < len(area) * len(area[0]):
        next_position = [position[0] + direction[0], position[1] + direction[1]]
        r, c = next_position
        if 0 <= r < len(area) and 0 <= c < len(area[0]) and area[r][c] != "O":
            if area[r][c] == "S":
                step.append(direction)
            position = next_position
        else:
            for d in directions:
                if d != direction and d != (direction[0]*(-1), direction[1]*(-1)):
                    pass

        passed.append(f"")



    if not found:
        return None
    return step



class TestIceCave(unittest.TestCase): 
    def test1(self):
        area = [[" "," "," "], 
                [" ","G"," "]]
        direction = "N"
        output = "D"
        self.assertEqual(iceCave(area, direction), output)

    def test2(self):
        area = [[" ","S"," ","O"], 
                ["G","S"," "," "], 
                ["O","O"," "," "]]
        direction = "S"
        output = "ULL"
        self.assertEqual(iceCave(area, direction), output)

    def test3(self):
        area = [["S"," "," ","S"," "," "," "," "," "," "], 
                [" "," "," "," "," "," "," "," "," "," "], 
                [" "," "," "," "," "," "," "," ","S"," "], 
                [" "," "," "," "," "," ","S"," "," "," "], 
                ["O"," "," "," "," "," "," "," ","O"," "], 
                [" "," "," "," "," "," "," "," ","S","O"], 
                [" "," ","O"," "," "," "," ","G"," "," "], 
                [" "," "," "," ","O"," "," ","O"," "," "], 
                [" ","O"," "," "," "," "," "," ","O"," "], 
                [" "," "," "," "," ","O"," "," "," "," "]]
        direction = "W"
        output = "RDRUL"
        self.assertEqual(iceCave(area, direction), output)

    def test4(self):
        area = [[" ","O"], 
                ["O","G"]]
        direction = "N"
        output = "impossible"
        self.assertEqual(iceCave(area, direction), output)

    def test5(self):
        area = [[" "," ","O","S"," ","G","O"," "," "," "], 
                [" "," "," ","O"," ","O","S"," "," "," "], 
                [" ","G","O"," "," "," ","O"," "," "," "], 
                ["O"," ","S"," ","O","O","S","O"," ","O"], 
                [" "," "," "," "," "," "," ","O"," "," "], 
                [" "," ","O"," ","O"," "," "," "," "," "], 
                ["O","G"," "," ","O"," "," "," "," ","O"], 
                [" "," ","O"," "," "," "," "," "," ","O"], 
                [" ","S","O"," "," ","S"," ","O"," "," "], 
                ["S"," ","S"," "," "," "," "," ","S","O"]]
        direction = "E"
        output = "LULDRD"
        self.assertEqual(iceCave(area, direction), output)

    def test6(self):
        area = [[" "," "," "," "," "," "," "," ","O"," "," "," "," "," "], 
                [" "," "," ","O"," "," "," "," "," "," "," "," "," "," "], 
                [" "," "," "," "," "," "," "," "," ","O"," "," "," "," "], 
                [" ","O"," "," "," "," "," "," "," "," "," "," "," "," "], 
                ["O"," "," "," "," "," "," "," ","O"," "," "," "," "," "], 
                [" "," "," "," "," "," "," "," "," "," "," "," "," ","O"], 
                [" "," "," "," "," "," ","O"," "," "," "," "," "," "," "], 
                [" "," ","O"," "," "," "," "," "," "," "," "," "," ","G"], 
                [" "," "," "," "," "," "," "," "," "," "," "," "," ","O"], 
                [" "," "," "," "," "," "," ","O"," "," "," "," "," "," "], 
                [" "," "," "," "," ","O"," "," "," ","O"," "," "," "," "], 
                [" "," "," "," "," "," "," "," "," "," "," "," "," "," "], 
                ["O","O","O","O","O","O","O","O","O","O","O","O","O"," "]]
        direction = "N"
        output = "ULURURDLULDRDRUR"
        self.assertEqual(iceCave(area, direction), output)

if __name__ == "__main__":
    unittest.main()