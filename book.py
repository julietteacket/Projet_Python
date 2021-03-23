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
    
    def sort_sell_orders(self):
        """ trie dans l'ordre croissant la liste des sell"""
        n = len(self.sell_orders)
        for i in range(n):
            for j in range(0,n-i-1):
                if self.sell_orders[j].price > self.sell_orders[j+1].price:
                    self.sell_orders[j], self.sell_orders[j+1] = self.sell_orders[j+1], self.sell_orders[j]
                if self.sell_orders[j].price == self.sell_orders[j+1].price:
                    if self.sell_orders[j].priority > self.sell_orders[j+1].priority:
                        self.sell_orders[j], self.sell_orders[j+1] = self.sell_orders[j+1], self.sell_orders[j]

    def sort_buy_orders(self):
        """trie dans l'ordre décroissant la liste des buy"""
        n = len(self.buy_orders)
        for i in range(n):
            for j in range(0,n-i-1):
                if self.buy_orders[j].price < self.buy_orders[j+1].price:
                    self.buy_orders[j], self.buy_orders[j+1] = self.buy_orders[j+1], self.buy_orders[j]
                if self.buy_orders[j].price ==self.buy_orders[j+1].price:
                    if self.buy_orders[j].priority > self.buy_orders[j+1].priority:
                        self.buy_orders[j],self.buy_orders[j+1] = self.buy_orders[j+1], self.buy_orders[j]

    


