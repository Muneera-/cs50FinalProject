class ShoppingCart(object):
	
	total = 0
	items = []

	def __init__(self):
	    
		self.total = 0
		self.items = []
    
	def addItem(self, cartItem):
		self.items.append(cartItem)
		
	def removeItem (self, cartItem):
		self.items.remove(cartItem)
	    