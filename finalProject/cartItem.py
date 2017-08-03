class CartItem(object):
    quantity = 0
    itemId = 0
    price = 0.0
    description = ""
    name = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, quantity, itemId, price):
        self.quantity = quantity
        self.itemId = itemId
        self.price = price
        self.description = ""
        self.name = ""