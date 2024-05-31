#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = []
  def add_item(self, title, price, quantity= 1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(title)
      self.last_transaction.append({
        "title": title, "quantity" : quantity, "price" : price
      })        

  def apply_discount(self):
    if self.discount:
      self.total = int(self.total * ((100 - self.discount) / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if not self.previous_transactions:
        return "There are no transactions to void."

    last_transaction = self.previous_transactions[-1]
    price = last_transaction["price"]
    quantity = last_transaction["quantity"]

    self.total -= price * quantity

    for _ in range(self.previous_transactions[-1]["quantity"]):
        self.items.pop()

    self.previous_transactions.pop()