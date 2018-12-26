"""
D
C
B
A
"""

class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()
	def get_stack(self):
		return self.items
	def is_empty(self):
		return self.items == [] # evaluates to true or false
	def peek(self):
		if not self.is_empty():
			return self.items[0]
	def end(self):
		if not self.is_empty():
			return self.items[-1]

s = Stack()
s.push("A")
s.push("B")
s.push("C")
print (s.get_stack())
s.pop()
s.push("D")
print (s.get_stack())
print(s.peek())
print (s.end())