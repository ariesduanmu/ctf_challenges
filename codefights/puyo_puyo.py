# -*- coding: utf-8 -*-
'''
Rules:

* Each piece is made up of two "Puyos", each coloured red, green, 
blue, yellow, or violet (could both be the same colour, but not necessarily). 
You are allowed to rotate the piece, and if it's placed horizontally on 
uneven terrain, the two Puyos may separate.

* If four or more Puyos are connected (either by left, right, up, or down, 
no diagonal), they are immediately cleared from the screen.

* All Puyos are bound by the force of gravity - any time a piece is dropped 
or a group of Puyos is cleared, all Puyos fall into the tightest stack possible.

* If the Puyos fall into a configuration where another group of four or more 
Puyos are connected, they again get cleared, and the cycle potentially continues. 
This is called a chain.

* If more than one group of puyos are cleared at once (without the fall of 
gravity in between), it doesn't count as a chain.

* Dropping the initial piece in such a way that it separates and falls 
doesn't count as a chain.

score = (total Puyos cleared) * (number of chains)

Given an array of strings field, representing what your playing field looks 
like at this point in the game, and a string nextPiece representing the piece 
(2 Puyos) you'll receive next, your task is to find the maximum score you 
can get from placing this piece.
'''
import unittest

def puyoPuyo(field, nextPiece):
    max_s = 0
    for offset in range(len(field[0])):
        for piece in [nextPiece, nextPiece[::-1]]:
            for d in ["h","v"]:
                fd = [list(f) for f in field]
                drop_new_piece(fd, piece, offset, d)
                s = score(fd)
                max_s = max(max_s, s)
    return max_s

def score(field):
    s = eliminate(field)
    i = 0
    total = 0
    while s != 0:
        i += 1
        total += s
        refresh(field)
        s = eliminate(field)
    return total * i

def eliminate(field):
    directors = ((0,1),(0,-1),(-1,0),(1,0))
    checked = set()
    eliminated = 0
    for i in range(len(field)):
        for j in range(len(field[0])):
            p = field[i][j]
            if p != " ":
                checking = set(["{},{}".format(i,j)])
                points = [[i,j]]
                while len(points) > 0:
                    next_point = []
                    for p_r, p_c in points:
                        for r, c in directors:
                            x, y = p_r+r, p_c+c
                            o = "{},{}".format(x,y)
                            if 0<=x<len(field) and 0<=y<len(field[0]) and field[x][y] == p and o not in checking:
                                checking.add(o)
                                next_point.append([x,y])
                            
                    points = next_point
                if len(checking) >= 4:
                    for c in checking:
                        x, y = c.split(",")
                        field[int(x)][int(y)] = " "
                    eliminated += len(checking)
    return eliminated

def refresh(field):
    for i in range(len(field)-2,-1,-1):
        for j in range(len(field[0])):
            p = field[i][j]
            if p != " ":
                gravity(field, p, (i,j)) 

def drop_new_piece(field, piece, offset, d="h"):
    if d == "h" and offset+1 < len(field[0]):
        gravity(field, piece[0], (-1,offset))
        gravity(field, piece[1], (-1,offset+1))
    elif d == "v":
        gravity(field, piece[0], (-1,offset))
        gravity(field, piece[1], (-1,offset))

def gravity(field, p, position):
    r, c = position
    for i in range(len(field)-1, r, -1):
        if field[i][c] == " ":
            field[i][c] = p
            if r != -1:
                field[r][c] = " "
            break

class PuyoPuyoTest(unittest.TestCase):
    def test_1(self):
        field = ["      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "  Y   ", 
                 "  Y   ", 
                 "  Y   ", 
                 "  B   ", 
                 "  BR  ", 
                 "GYYBR ", 
                 "GGYBR "]
        nextPiece = "YG"
        score = 36
        self.assertEqual(puyoPuyo(field, nextPiece), score)

    def test_2(self):
        field = ["      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "YYYVVV"]
        nextPiece = "YV"
        score = 16
        self.assertEqual(puyoPuyo(field, nextPiece), score)

    def test_3(self):
        field = ["      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "    B ", 
                 "  R B ", 
                 "  RGB ", 
                 "  RBY ", 
                 " RGBY ", 
                 " RGBY "]
        nextPiece = "GY"
        score = 76
        self.assertEqual(puyoPuyo(field, nextPiece), score)

    def test_4(self):
        field = ["      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 " BBBGG"]
        nextPiece = "BG"
        score = 4
        self.assertEqual(puyoPuyo(field, nextPiece), score)

    def test_5(self):
        field = ["      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      "]
        nextPiece = "VV"
        score = 0
        self.assertEqual(puyoPuyo(field, nextPiece), score)

    def test_6(self):
        field = ["      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "R Y   ", 
                 "G R   ", 
                 "B VY  ", 
                 "B BG Y", 
                 "V VRRG"]
        nextPiece = "VB"
        score = 16
        self.assertEqual(puyoPuyo(field, nextPiece), score)

    def test_7(self):
        field = ["      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "  V   ", 
                 "YYYVVV"]
        nextPiece = "YV"
        score = 18
        self.assertEqual(puyoPuyo(field, nextPiece), score)

    def test_8(self):
        field = ["      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 "      ", 
                 " B Y  ", 
                 " B Y  ", 
                 " B Y  "]
        nextPiece = "BY"
        score = 8
        self.assertEqual(puyoPuyo(field, nextPiece), score)

    def test_9(self):
        field = ["      ", 
                 "      ", 
                 "   G  ", 
                 "   G  ", 
                 "   R  ", 
                 " B R  ", 
                 " B R  ", 
                 " B VG ", 
                 " R YV ", 
                 " GRYVG", 
                 "GGVBYV", 
                 "RRBBYV"]
        nextPiece = "RG"
        score = 192
        self.assertEqual(puyoPuyo(field, nextPiece), score)

if __name__ == "__main__":
    unittest.main()