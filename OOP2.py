
class Employee:
	num_of_emp = 0
	raise_amount = int(3)

	def __init__(self, pay, first, last): #initialize. Will load the attributes
		self.pay = pay
		self.first = first
		self.last = last
		self.email = f'{first}{last}@company.com'

		Employee.num_of_emp +=1
	def generate_name(self): # a method (a function that belongs to a class)
		return f'{self.first} {self.last}' 
	
	def pay_bump(self):
 		self.pay = int(self.pay * self.raise_amount)
 	
	@classmethod
	def set_raise_amt(cls, amount):
 		cls.raise_amount = amount
	@classmethod
	def from_string(cls, emp_str):
 		first, last, pay = emp_str.split('-')
 		return cls(first, last, pay)


# class is a blue print for creating instances

emp_1 = Employee(50000, "Robert", "Neuzil")
emp_2 = Employee(44444444444, "Jacob", "Schmidt")

Employee.set_raise_amt(1.05)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = "Steve-Smith-40000"
emp_str_3 = "Jane-Doe_90000"

emp_3 = Employee.from_string(emp_str_1)







