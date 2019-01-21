# -*- coding: utf-8 -*-

class FPSMap():
    def __init__(self, width=100, height=50):
        self.board = [["."]*width for _ in range(height)]
        
        for i in range(20, 81):
            for j in range(15, 36):
                self.board[j][i] = " "

        for j in range(35, 66):
            for i in list(range(10, 16)) + list(range(35, 41)):
                self.board[i][j] = " "

        self.AI = (36, 25)
        self.board[self.AI[0]][self.AI[1]] = "x"


    def __str__(self):
        return "\n".join("".join(b) for b in self.board)



