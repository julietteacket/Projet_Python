class Book:
    def __init__(self, name, buy_orders = [], sell_orders = []):
        """buy_orders and sell_orders are lists"""
        self.name = name
        self.buy_orders = buy_orders
        self.sell_orders = sell_orders 

    def insert_order(self, quantity, price, side):
        o = Order(quantity, price, side)
        if side : #it's a buy
            self.buy_orders.append(o)
        else : #it's a sell
            self.sell_orders.append(o)
    
    #def sort_buy_orders
    #def sort_sell_orders
    


