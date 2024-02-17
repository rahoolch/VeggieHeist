# This class is an extended class to creature class as captain is also a creature on the field
# which is going to move according to the key we press

from Creature import Creature

class Captain(Creature):

    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self._basket = [] # basket for collection of veggies

    def add_veggies(self,veggie):
        self._basket.append(veggie)

    def get_basket(self):
        return self._basket
    
    def set_basket(self, basket):
        self._basket = basket
        
