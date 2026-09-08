#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount: int = 0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item: str, price: float, quantity: int = 1):
        item_total_cost = float(price) * quantity
        self.total += item_total_cost
        
        for _ in range(quantity):
            self.items.append(item)
        
        transaction_record = {
            "item": item,
            "quantity": quantity,
            "total_cost": item_total_cost
        }
        self.previous_transactions.append(transaction_record)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_multiplier = self.discount / 100
        discount_amount = self.total * discount_multiplier
        self.total -= discount_amount
        
        formatted_total = int(self.total) if self.total.is_integer() else self.total
        print(f"After the discount, the total comes to ${formatted_total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_tx = self.previous_transactions.pop()
        self.total -= last_tx["total_cost"]
        
        for _ in range(last_tx["quantity"]):
            if last_tx["item"] in self.items:
                self.items.remove(last_tx["item"])
