# -*- coding: utf-8 -*-
from enum import Enum

class AIStatus(Enum):
    PASSIVE = 0
    AGGRESSIVE = 1
    DEFENSIVE = 2

class AI():
    def __init__(self):
        self.health = 100
        self.state = AIStatus.PASSIVE

    def cover_fire(self):
        self

    def move2cover(self):
        pass

    def backward_fire(self):
        pass

    def front_fire(self):
        pass

    def walk_around(self):
        pass

    def attacked(self, hurt):
        self.health = max(0, self.health-hurt)
