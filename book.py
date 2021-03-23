from order import Order


class Book:
    def __init__(self, name, buy_orders = [], sell_orders = [], nb_orders = 0):
        """buy_orders and sell_orders are lists"""
        self.name = name
        self.buy_orders = buy_orders
        self.sell_orders = sell_orders 
        self.nb_orders = len(self.buy_orders) + len(self.sell_orders)

    def insert_buy(self, quantity, price):
        o = Order(quantity, price)
        o.priority = self.nb_orders +1
        self.nb_orders += 1
        self.buy_orders.append(o)
        
    def insert_sell(self, quantity, price):
        o = Order(quantity, price)
        o.priority = self.nb_orders + 1
        self.nb_orders += 1
        self.sell_orders.append(o)
    
    #def sort_buy_orders
    #def sort_sell_orders
    


