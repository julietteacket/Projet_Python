#!/usr/bin/env python3
from order import Order
import pandas as pd

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
        print("---Insert BUY " + str(o) + " id=" + str(o.priority) + " on " + self.name)
        restant = self.execute_buy_orders(quantity, price)
        if restant != 0:
            o.quantity = restant
            self.buy_orders.append(o)
        print(str(self))
        dataframe = self.create_dataframe()
        print(dataframe)
        
    def insert_sell(self, quantity, price):
        o = Order(quantity, price)
        o.priority = self.nb_orders + 1
        self.nb_orders += 1
        print("--- Insert SELL " + str(o) + " id=" + str(o.priority) + " on " + self.name)
        restant = self.execute_sell_orders(quantity, price)
        if restant != 0:
            o.quantity = restant
            self.sell_orders.append(o)
        print(str(self))
        dataframe = self.create_dataframe()
        print(dataframe)
        

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

    def __str__(self):
        affich = "Book on " + self.name + "\n"
        self.sort_sell_orders()
        for i in range(len(self.sell_orders)):
            affich += "        SELL " + str(self.sell_orders[i]) + " id=" + str(self.sell_orders[i].priority) + "\n"
        self.sort_buy_orders()
        for j in range(len(self.buy_orders)):
            affich += "        BUY " + str(self.buy_orders[j]) + " id=" + str(self.buy_orders[j].priority) + "\n"
        affich += "---------------------------------"
        return affich

    def execute_buy_orders(self, quantity, price):
        """quand on ajoute un ordre buy, on regarde dans la liste des sell si on peut faire une transaction. On renvoie le nombre de buy qu'il reste"""
        for i in range(len(self.sell_orders)):
            if (self.sell_orders[i].price <= price) and (quantity>0):
                evalable = min(quantity, self.sell_orders[i].quantity)
                quantity = quantity - evalable
                self.sell_orders[i].quantity = self.sell_orders[i].quantity - evalable
                print("Execute " + str(evalable) + " at " + str(self.sell_orders[i].price) + " on " + self.name)
        new_sell_orders = []
        for j in range(len(self.sell_orders)):
            if self.sell_orders[j].quantity != 0 :
                new_sell_orders.append(self.sell_orders[j])
        self.sell_orders = new_sell_orders
        return quantity

    def execute_sell_orders(self, quantity, price):
        """quand on ajoute un ordre sell, on regarde dans la liste des buy si on peut faire une transaction. On renvoie le nombre de sell qu'il reste"""
        for i in range(len(self.buy_orders)):
            if (self.buy_orders[i].price >= price) and (quantity>0):
                evalable = min(quantity, self.buy_orders[i].quantity)
                quantity = quantity - evalable
                self.buy_orders[i].quantity = self.buy_orders[i].quantity - evalable
                print("Execute " + str(evalable) + " at " + str(self.buy_orders[i].price) + " on " + self.name)
        new_buy_orders = []
        for j in range(len(self.buy_orders)):
            if self.buy_orders[j].quantity != 0 :
                new_buy_orders.append(self.buy_orders[j])
        self.buy_orders = new_buy_orders
        return quantity

    def create_dataframe(self):
        df = pd.DataFrame(columns=['Priority','Type','Price','Quantity'])
        for i in range (len(self.buy_orders)):
            df.loc[i] = [self.buy_orders[i].priority,"Buy", self.buy_orders[i].price, self.buy_orders[i].quantity] 
        for j in range(len(self.buy_orders),len(self.buy_orders)+len(self.sell_orders)):
            df.loc[j] = [self.sell_orders[j-len(self.buy_orders)].priority,"Sell", self.sell_orders[j-len(self.buy_orders)].price, self.sell_orders[j-len(self.buy_orders)].quantity] 
        return df
        
 




    

