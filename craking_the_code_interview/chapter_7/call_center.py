class Employee:
	def __init__(self):
		self.available = True

	def set_work(self):
		self.available = False

	def set_rest(self):
		self.available = True
		
	def is_available(self):
		return self.available



# third layer: fresher
class Fresher(Employee):
	def __init__(self):
		self.available = True



# second layer: technical lead
class TechnicalLead(Employee):
	def __init__(self):
		self.available = True



# first layer: product manager
class ProductManager(Employee):
	def __init__(self):
		self.available = True



class CallCenter:
	def __init__(self, product_manager, technical_lead, freshers):
		self.product_manager = product_manager
		self.technical_lead = technical_lead
		self.freshers = freshers

	def get_call_handler(self):
		for f in self.freshers:
			if f.is_available():
				return f

		if self.technical_lead.is_available():
			return self.technical_lead

		if self.product_manager.is_available():
			return self.product_manager

		return None