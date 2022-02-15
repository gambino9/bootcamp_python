# getattr(object, name[, default])
# Return the value of the named attribute of object. name must be a string.
# If the string is the name of one of the object’s attributes, the result is
# the value of that attribute.

# setattr(object, name, value)
# This is the counterpart of getattr(). The arguments are an object, a string
# and an arbitrary value. The string may name an existing attribute or a new
# attribute. The function assigns the value to the attribute, provided
# the object allows it.

def what_are_the_vars(*args, **kwargs):
	"""
		fix the corrupted account
		@param args:
		@param kwargs:

		@return: an instance of class ObjectC
				None if an attribute we try to set already exists
	"""
	obj = ObjectC()
	ind = 0
	tmp = None
	for i in args:  # args
		setattr(obj, f"var_{ind}", str(i))
		ind += 1
	for k, v in kwargs.items():  # kwargs
		if hasattr(obj, k):
			setattr(obj, f"var_{ind - 1}", str(tmp))
			return None
		setattr(obj, k, v)
	return obj


class ObjectC(object):
	def __init__(self):
		pass


def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print(f"{attr}: {value}")
	print("end")


if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars(None, [])
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
	doom_printer(obj)
