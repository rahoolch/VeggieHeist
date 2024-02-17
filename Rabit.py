
# Class extending Creature to put the rabits on the place and also update their location
# on every move.

from Creature import Creature

class Rabit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")


