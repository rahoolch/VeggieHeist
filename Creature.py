# Class to define and retrieve information of the creatures on the field.

from FieldInhabitant import FieldInhabitant
# extended class of FieldInhabitant to put positions of rabits and captain

# this class is useful as the captain as well as rabits are moving so to
# update their location we can use this class

class Creature(FieldInhabitant):
    def __init__(self,x,y,symbol):
        super().__init__(symbol)
        # coordinates of the creatures.
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self,x):
        self._x = x

    def set_y(self,y):
        self._y = y
