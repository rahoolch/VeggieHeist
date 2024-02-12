
# class for all the field inhabitants -- Veggies


class FieldInhabitant:
    """Defining base class for object
        inhabitants in the field"""
    def __init__(self, symbol):
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol