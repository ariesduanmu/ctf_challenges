'''
Game Map

--------------------------------
|            ________          |
|       ____|        |___      |
|      |                 |     |
|      |         X       |     |
|      |_  _          ___|     |
|        AI |________|         |
|                     User     |
--------------------------------

Chance

Time      | Guard | Drink/Eat | Walk
---
Morning   | 0.87  | 0.1       | 0.03
Afternoon | 0.48  | 0.32      | 0.2
Night     | 0.35  | 0.4       | 0.25
'''
from enum import Enum

class AIStatus(Enum):
    PASSIVE = 0
    AGGRESSIVE = 1
    DEFENSIVE = 2

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

class AI():
    def __init__(self):
        self.health = 100
        self.state = AIStatus.PASSIVE

    def cover_fire(self):
        pass

    def move2cover(self):
        pass

    def backward_fire(self):
        pass

    def front_fire(self):
        pass

    def walk_around(self):
        pass

class User():
    def __init__(self):
        pass

class Game():
    def __init__(self):
        self.map = FPSMap()

    def defensive(self):
        if self.user.position == "triggerR":
            if self.ai.cover:
                self.ai.cover_fire()
            else:
                self.ai.move2cover()
        elif self.user.position == "triggerM":
            self.ai.backward_fire()

    def aggressive(self):
        if self.user.position == "triggerL" or self.user.position == "triggerM":
            self.ai.front_fire()
        else:
            self.ai.walk_around()



if __name__ == "__main__":
    print(FPSMap())


