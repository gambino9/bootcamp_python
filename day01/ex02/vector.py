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

	# Overloading many operators here using 'magic methods' (built-in functions) :
	def __add__(self, other):
		""" Only Vectors of same dimension"""
		if isinstance(other, Vector):
			if self.shape != other.shape:
				raise VectorError("The Vectors must be of the same shape")
			if self.row_vector:
				vector_data = [a + b for a, b in zip(self.values, other.values)]
			else:
				vector_data = [[i + j for i, j in zip(a, b)] for a, b in zip(self.values, other.values)]
			vector_obj = Vector(vector_data)
			return vector_obj
		else:
			return NotImplemented("Cannot add a Vector with a non Vector object")

	def __radd__(self, other):
		""" Only Vectors of same dimension"""
		if not isinstance(other, Vector):
			return NotImplemented("Cannot add a Vector with a non Vector object")
		else:
			return other.__add__(self.values)

	def __sub__(self, other):
		""" Only Vectors of same dimension"""
		if isinstance(other, Vector):
			if self.shape != other.shape:
				raise VectorError("The Vectors must be of the same shape")
			if self.row_vector:
				vector_data = [a - b for a, b in zip(self.values, other.values)]
			else:
				vector_data = [[i - j for i, j in zip(a, b)] for a, b in zip(self.values, other.values)]
			vector_obj = Vector(vector_data)
			return vector_obj
		else:
			return NotImplemented("Cannot sub a Vector with a non Vector object")

	def __rsub__(self, other):
		""" Only Vectors of same dimension"""
		if not isinstance(other, Vector):
			return NotImplemented("Cannot rsub a Vector with a non Vector object")
		else:
			return other.__sub__(self.values)

	def __truediv__(self, other):
		""" Only scalars"""
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
		""" Only scalars"""
		if type(other) == int or type(other) == scalars:
			print("rsub")
			add_list = []
			for i in self.values:
				add_list.append(i / other)
			new_vec = Vector(add_list)
			return (new_vec)

	def __mul__(self, other):
		""" Only scalars"""
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
		""" Only scalars"""
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
