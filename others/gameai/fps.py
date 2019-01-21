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


