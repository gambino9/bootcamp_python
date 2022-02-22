import numpy as np


class NumPyCreator:
	def __init__(self):
		pass

	def from_list(self, lst):
		if not isinstance(lst, list) or not all(len(i) == len(lst[0]) for i in lst):
			return None
		return np.array(lst)

	def from_tuple(self, tpl):
		if not isinstance(tpl, tuple) or not all(len(i) == len(tpl[0]) for i in tpl):
			return None
		return np.array(tpl)

	def from_iterable(self, itr):
		try:
			iter(itr)
		except TypeError:
			return None
		return np.fromiter(itr, int)

	def from_shape(self, shape, value=0.):
		if any(i < 0 for i in shape):
			return None
		return np.full(shape, value)

	def random(self, shape):
		if any(i < 0 for i in shape):
			return None
		return np.random.random(shape)
	
	def identity(self, n):
		if n < 0:
			return None
		return np.identity(n)
