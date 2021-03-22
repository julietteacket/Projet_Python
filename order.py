from functools import total_ordering

@total_ordering
class Order :
    def __init__(self, quantity, price,side=True):
        """side = True if it's a buy"""
        self.quantity = quantity
        self.price = price
        self.side = side

    def is_sell(self):
        #returns False (= not buy) is sell order
        return not self.buy

   # def quantity(self):
   #     return self.quantity if self.buy else -self.quantity

    def __str__(self):
        """human-readable content"""
        return "%s @ %s"  % (self.quantity, self.price)

    def __repr__(self):
        """unambiguous representation of the object"""
        return "Order(%s, %s)" % (self.quantity, self.price)

    def __eq__(self, other):
        """self == other ?"""
        return other and self.quantity == other.quantity and self.price == other.price

    def __lt__(self, other):
        """self < other ?"""
        return other and self.price < other.price
