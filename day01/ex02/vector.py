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
		if isinstance(other, (int, float)):
			if self.row_vector:
				result = [a / other for a in self.values]
			else:
				result = [[a / other for a in i] for i in self.values]
			scalar_div_obj = Vector(result)
			return scalar_div_obj
		else:
			return NotImplemented("A Vector object can only be divided by a scalar")

	def __rtruediv__(self, other):
		""" Only scalars"""
		raise VectorError("A scalar can't be divided by a matrix")

	def __mul__(self, other):
		""" Only scalars"""
		if isinstance(other, (int, float)):
			if self.row_vector:
				result = [a * other for a in self.values]
			else:
				result = [[a * other for a in i] for i in self.values]
			scalar_mult_obj = Vector(result)
			return scalar_mult_obj
		else:
			return NotImplemented("A Vector object can only be divided by a scalar")

	def __rmul__(self, other):
		""" Only scalars"""
		if not isinstance(other, Vector):
			return NotImplemented("Cannot multiply a Vector with a non Vector object")
		else:
			return other.__mul__(self.values)

	def __str__(self):
		""" 
		Link explaining in detail str and repr methods : 
		https://stackoverflow.com/questions/1436703/difference-between-str-and-repr/2626364#2626364
		__repr__ goal is to be unambiguous (purpose of development, debugging, etc...)
		__str__ goal is to be readable
		"""
		return f"This {self.__class__.__name__} object contains the following " \
			   f"values : ({self.values}) and is of shape : {self.shape}"

	def __repr__(self):
		return f"{str(self.__class__.__name__)}({self.values})"

	def dot(self, v):
		pass

	def t(self, v):
		pass
