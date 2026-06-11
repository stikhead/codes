class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_item(self, name, price):
        self._items.append({"name": name, "price": price})
    
    @property
    def total_price(self):
        return sum(map(lambda x: x["price"], self._items), 0)

cart = ShoppingCart()
cart.add_item("appple", 2)
cart.add_item("laptop", 1000)

print(cart.total_price)

        