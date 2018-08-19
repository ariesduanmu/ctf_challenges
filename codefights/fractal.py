# -*- coding: utf-8 -*-
'''
Your task is to draw a special fractal after n iterations. The fractal consists of unit connectors '|' and '_'.

For n = 1 the fractal looks as follows:

_
_|
Now assume that you have already made N iterations and drawn the f(N) fractal. To draw the f(N + 1) fractal do the following:
Note that every fractal has exactly two edge points which can be connected to the edge points of other fractals using the unit connectors.
At first, take the f(N) fractal and place it in the top left corner. As the next step, put f(N) rotated by 0°, 90°, 180° or 270° in the remaining 3 quarters - top right, bottom left and bottom right - so that it is possible to connect all four of them by adding exactly 3 unit connectors between the adjacent fractal edge points.
Note that there is always exactly one possible combination of rotations which allows to connect all 4 f(N) fractals together.

See examples below for better understanding.

Example

For n = 1, the output should be

[[' ', '_', ' '],       
 [' ', '_', '|']]       
 
In other words, it should represent      _
the following picture:                   _| 
For n = 2, the output should be

[[' ', '_', ' ', ' ', ' ', '_', ' '],      
 [' ', '_', '|', ' ', '|', '_', ' '],                                  
 ['|', ' ', ' ', '_', ' ', ' ', '|'],                                 
 ['|', '_', '|', ' ', '|', '_', '|']]

Or, to put it differently:  _   _
                            _| |_
                           |  _  |
                           |_| |_| 
For n = 3, the fractal looks as follows:

                      _   ___   ___ 
                      _| |_  |_|  _|
                     |  _  |  _  |_ 
                     |_| |_| | |___|
                      _   _  |  ___ 
                     | |_| | |_|  _|
                     |_   _|  _  |_ 
                      _| |___| |___|
For n = 4, the fractal looks as follows:

               _   ___   ___   ___   ___   _ 
               _| |_  |_|  _| |_  |_|  _| |_ 
              |  _  |  _  |_   _|  _  |  _  |
              |_| |_| | |___| |___| | |_| |_|
               _   _  |  ___   ___  |  _   _ 
              | |_| | |_|  _| |_  |_| | |_| |
              |_   _|  _  |_   _|  _  |_   _|
               _| |___| |___| |___| |___| |_ 
              |  ___   ___   _   ___   ___  |
              |_|  _| |_  |_| |_|  _| |_  |_|
               _  |_   _|  _   _  |_   _|  _ 
              | |___| |___| | | |___| |___| |
              |_   _____   _| |_   _____   _|
               _| |_   _| |_   _| |_   _| |_ 
              |  _  | |  _  | |  _  | |  _  |
              |_| |_| |_| |_| |_| |_| |_| |_|
'''

import unittest

def fractal(n):
    if n == 1:
        return [[" ","_"," "], 
                [" ","_","|"]]
    shape = fractal(n-1)
    shape = decompress_shape(shape)
    r, c = len(shape), len(shape[0])
    U,L,B,R = all_directions(shape)
    # U_points = open_points(U)
    # L_points = open_points(L)
    # B_points = open_points(B)
    # R_points = open_points(R)
    if n % 2 == 0:
        conjects = [[r, 0, "|"], [r, c * 2, "|"], [r + 1, c, "_"]]
        return compress_shape(combine(U, B, L, L, conjects))
    else:
        conjects = [[0, c, "_"], [0, c-1, "_"], [r * 2, c , "_"], [r * 2, c-1 , "_"], [r, c + 1, "|"]]
        return compress_shape(combine(U, R, B, R, conjects))

def combine(shape1, shape2, shape3, shape4, conjects):
    n, m = len(shape1), len(shape1[0])
    shape = [[" " for _ in range(m * 2 + 1)] for _ in range(n * 2 + 1)]
    for i in range(n):
        for j in range(m):
            shape[i][j] = shape1[i][j]
            shape[i][j+m+1] = shape2[i][j]
            shape[i+n+1][j] = shape3[i][j]
            shape[i+n+1][j+m+1] = shape4[i][j]
    for r, c, s in conjects:
        shape[r][c] = s
    return shape

def open_points(shape):
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1))
    points = []
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == "|" or shape[i][j] == "_":
                connection = 0
                for direction in directions:
                    r, c = i + direction[0]. j + direction[1]
                    if 0 <= r < len(shape) and 0 <= c < len(shape[0]) and shape[i][j] != " ":
                        connection += 1
                if connection == 1:
                    points += [[i, j]]
    return points

def all_directions(shape):
    shape1 = zip(*shape[::-1])
    shape2 = zip(*shape1[::-1])
    shape3 = zip(*shape2[::-1])
    return shape, switch_shape(shape1), shape2, switch_shape(shape3)

def switch_shape(shape):
    tmp1 = [[":" if k == "_" else k for k in s] for s in shape]
    tmp2 = [["_" if k == "|" else k for k in s] for s in tmp1]
    return [["|" if k == ":" else k for k in s] for s in tmp2]

def compress_shape(shape):
    compressed_shape = []
    tmp = None
    for s in shape:
        if "_" in s:
            if tmp is None:
                compressed_shape.append(s)
            else:
                k = [s[i] if s[i] == "_" else tmp[i] for i in range(len(s)) ]
                compressed_shape.append(k)
                tmp = None
        elif "|" in s:
            tmp = s
    
    if tmp is not None:
        compressed_shape.append(tmp)
       
    return compressed_shape

def decompress_shape(shape):
    horizontal = None
    decompressed_shape = []
    for s in shape:
        if "_" in s and "|" not in s:
            decompressed_shape.append(s)
            horizontal = True
        elif "|" in s and "_" not in s:
            decompressed_shape.append(s)
            horizontal = False
        else:
            s1 = [i if i == "|" else " " for i in s]
            s2 = [i if i == "_" else " " for i in s]
            if horizontal:
                decompressed_shape.append(s1)
                decompressed_shape.append(s2)
            else:
                decompressed_shape.append(s2)
                decompressed_shape.append(s1)
    return decompressed_shape

class TestFractal(unittest.TestCase): 
    def test1(self):
        output = [[" ","_"," "], 
                  [" ","_","|"]]
        n = 1
        self.assertEqual(fractal(n), output)

    def test2(self):
        output = [[" ","_"," "," "," ","_"," "], 
                  [" ","_","|"," ","|","_"," "], 
                  ["|"," "," ","_"," "," ","|"], 
                  ["|","_","|"," ","|","_","|"]]
        n = 2
        self.assertEqual(fractal(n), output)

    def test3(self):
        output = [[" ","_"," "," "," ","_","_","_"," "," "," ","_","_","_"," "], 
                  [" ","_","|"," ","|","_"," "," ","|","_","|"," "," ","_","|"], 
                  ["|"," "," ","_"," "," ","|"," "," ","_"," "," ","|","_"," "], 
                  ["|","_","|"," ","|","_","|"," ","|"," ","|","_","_","_","|"], 
                  [" ","_"," "," "," ","_"," "," ","|"," "," ","_","_","_"," "], 
                  ["|"," ","|","_","|"," ","|"," ","|","_","|"," "," ","_","|"], 
                  ["|","_"," "," "," ","_","|"," "," ","_"," "," ","|","_"," "], 
                  [" ","_","|"," ","|","_","_","_","|"," ","|","_","_","_","|"]]
        n = 3
        self.assertEqual(fractal(n), output)

if __name__ == "__main__":
    #unittest.main()
    shape = fractal(3)
    print("\n".join("".join(s) for s in shape))

    # output = [[" ","_"," "," "," ","_","_","_"," "," "," ","_","_","_"," "], 
    #               [" ","_","|"," ","|","_"," "," ","|","_","|"," "," ","_","|"], 
    #               ["|"," "," ","_"," "," ","|"," "," ","_"," "," ","|","_"," "], 
    #               ["|","_","|"," ","|","_","|"," ","|"," ","|","_","_","_","|"], 
    #               [" ","_"," "," "," ","_"," "," ","|"," "," ","_","_","_"," "], 
    #               ["|"," ","|","_","|"," ","|"," ","|","_","|"," "," ","_","|"], 
    #               ["|","_"," "," "," ","_","|"," "," ","_"," "," ","|","_"," "], 
    #               [" ","_","|"," ","|","_","_","_","|"," ","|","_","_","_","|"]]
    # print("\n".join("".join(s) for s in output))






