d = {}

# dictionary keys treat integers and strings differently
d[1] = 'yes'
d['1'] = 'no'
d[2] = 90000000000

class MyClass:
	def __init__(self):
		self.data = 'data'

#create an instance of class

instance = MyClass()

#can store the instance in a dictionary
d['object'] = instance

d['object'].data

