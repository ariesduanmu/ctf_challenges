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
    pass

def pieces(piece):
    a = piece[0]
    b = piece[1]
    if a == b:
        return [[[a,b]],[[a],[b]]]
    return [[[a,b]],[[a],[b]],[[b,a]],[[b],[a]]]

def drop(field, piece, offset):
    pass

def test():
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


class PuyoPuyoTest(unittest.TestCase):
    def test_1:
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