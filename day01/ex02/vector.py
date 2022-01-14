# Creating Vector class that initializes a vector object in 3 differents way :
# - a list of floats : Vector([0.0, 1.0, 2.0, 3.0])
# - a size of Vector(3) --> vector.values = [0.0, 1.0, 2.0]
# - a range of Vector((10. 14)) --> vector.values = [10.0, 11.0, 12.0, 13.0]
class VectorError(Exception):
	""" Exception class for Matrix"""
	pass


class Vector:
	def __init__(self, arg):
		self.values = None
		self.shape = None
		self.row_vector = False

		if isinstance(arg, (range, tuple, int)):
			if isinstance(arg, int):
				float_range = range(0, arg)
			elif isinstance(arg, tuple):
				float_range = range(*arg)
			else:
				float_range = arg
			self.values = [[float(elem)] for elem in float_range]
		elif isinstance(arg, list):
			if all(isinstance(elem, list) for elem in arg):
				for sub_list in arg:
					if not all(isinstance(sub_elem, float) for sub_elem in sub_list):
						raise VectorError("List must contains floats only")
			else:
				if not all(isinstance(elem, float) for elem in arg):
					raise VectorError("List must contains floats only")
				self.row_vector = True
			self.values = arg
		self.shape = ((1, len(self.values)) if self.row_vector else (len(self.values), 1))


		# if values != None:
		# 	if type(values) == list:
		# 		for i in values:
		# 			if (type(i) != float):
		# 				print("List must contain floats only")
		# 				exit()
		# 		self.values = values
		# 		self.size = len(values)
		# 	elif type(values) == int:
		# 		self.size = values
		# 		# init = float(0.0)
		# 		float_list = []
		# 		for i in range(0, self.size):
		# 			float_list.append(float(i))
		# 		self.values = float_list
		# 	elif type(values) == tuple and len(values) == 2:
		# 		float_list = [i * 1.0 for i in range(values[0], values[1])]
		# 		self.values = float_list
		# 		self.size = len(self.values)
		# elif values == None:
		# 	print("Please enter values, a size, or a range of vector")
		# 	exit()

# Overloading many operators here using 'magic methods' (built-in functions) :
	def __add__(self, other):
		if type(other) == int or type(other) == float:
			add_list = []
			for i in self.values:
				add_list.append(i + other)
			new_vec = Vector(add_list)
			print("add")
			return (new_vec)
		elif type(other) == Vector:
			print("add 2 vectors")
			add_list = []
			min_size = min(len(self.values), len(other.values))
			for i in range(0, min_size):
				add_list.append(self.values[i] + other.values[i])
			new_vec = Vector(add_list)
			return (new_vec)
	
	def __radd__(self, other):
		if type(other) == int or type(other) == float:
			print("radd")
			add_list = []
			for i in self.values:
				add_list.append(i + other)
			new_vec = Vector(add_list)
			return (new_vec)
	
	def __sub__(self, other):
		if type(other) == int or type(other) == float:
			add_list = []
			for i in self.values:
				add_list.append(i - other)
			new_vec = Vector(add_list)
			print("sub")
			return (new_vec)
		elif type(other) == Vector:
			print("sub 2 vectors")
			add_list = []
			min_size = min(len(self.values), len(other.values))
			for i in range(0, min_size):
				add_list.append(self.values[i] - other.values[i])
			new_vec = Vector(add_list)
			return (new_vec)
	
	def __rsub__(self, other):
		if type(other) == int or type(other) == float:
			print("radd")
			add_list = []
			for i in self.values:
				add_list.append(i - other)
			new_vec = Vector(add_list)
			return (new_vec)

	def __truediv__(self, other):
		if type(other) == int or type(other) == float:
			add_list = []
			for i in self.values:
				add_list.append(i / other)
			new_vec = Vector(add_list)
			print("sub")
			return (new_vec)
		else:
			print("Division only with scalars")

	def __rtruediv__(self, other):
		if type(other) == int or type(other) == scalars:
			print("rsub")
			add_list = []
			for i in self.values:
				add_list.append(i / other)
			new_vec = Vector(add_list)
			return (new_vec)
		
	def __mul__(self, other):
		if type(other) == int or type(other) == float:
			print("mul")
			add_list = []
			for i in self.values:
				add_list.append(i * other)
			new_vec = Vector(add_list)
			return (new_vec)
		elif type(other) == Vector:
			print("mul 2 vectors")
			add_list = []
			min_size = min(len(self.values), len(other.values))
			for i in range(0, min_size):
				add_list.append(self.values[i] * other.values[i])
			new_vec = Vector(add_list)
			return (new_vec)

	def __rmul__(self, other):
		if type(other) == int or type(other) == float:
			print("rmul")
			add_list = []
			for i in self.values:
				add_list.append(i * other)
			new_vec = Vector(add_list)
			return (new_vec)

	def __str__(self):
		""" 
		Link explaining in detail str and repr methods : 
		https://stackoverflow.com/questions/1436703/difference-between-str-and-repr/2626364#2626364
		""" 
		pass

	def __repr__(self):
		pass
