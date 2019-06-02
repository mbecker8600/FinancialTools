

class Trade:

    def __init__(self, sym, action, quantity):
        self.sym = sym
        self.action = action
        self.quantity = quantity

    def __str__(self):
        return "Symbol: {} Action: {} Quantity: {}".format(self.sym, self.action, self.quantity)
