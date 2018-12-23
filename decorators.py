def mydecorater(f):
	def wrapper():
		print ("Inside of the decorator before calling the function")
		f()
		print("Inside of the decorator after calling the function")
	return wrapper


@mydecorater
def print_name():
	print ("Robert")


print_name()