import sys


def ft_reduce(function_to_apply, iterable):
	"""
		Apply function of two arguments cumulatively.
		Args:
		function_to_apply: a function taking an iterable.
		iterable: an iterable object (list, tuple, iterator).
		Returns:
		A value, of same type of elements in the iterable parameter.
		None if the iterable can not be used by the function.
	"""
	try:
		if not callable(function_to_apply):
			raise TypeError("First parameter is not a function")
		iter(iterable)
		list_len = len(iterable)
		res = iterable[0]
		for i in range(1, list_len):
			res = function_to_apply(res, iterable[i])
		return res
	except TypeError as e:
		sys.exit(e)


if __name__ == "__main__":
	# Example3:
	lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
	print(ft_reduce(lambda u, v: u + v, lst))
	# Output:
	# "Hello world"
