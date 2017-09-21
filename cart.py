class Cart:

	def __init__(self, user_id):
		self.user_id = user_id
		self.items = []

	def add(self, product, qty):
		# book (4$) 2 8$
		self.items.append([product, qty, product.price * qty])

	def delete(self, product, qty=-100):
		cart_item_names = [item[0].name for item in self.items]
		index_of_product = cart_item_names.index(product.name)
		if qty == -100:
			del self.items[index_of_product]
		else:
			self.items[index_of_product][1] -= qty
			self.items[index_of_product][2] -= qty * self.items[index_of_product][0].price




	def grand_total(self):
		return sum([item[2] for item in self.items])


