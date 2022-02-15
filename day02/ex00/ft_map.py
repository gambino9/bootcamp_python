# https://book.pythontips.com/en/latest/map_filter.html

import sys

def ft_map(function_to_apply, iterable):
	"""
		Map the function to all elements of the iterable.
		Args:
		function_to_apply: a function taking an iterable.
		iterable: an iterable object (list, tuple, iterator).
		Returns:
		An iterable.
		None if the iterable can not be used by the function.
	"""
	try:
		if not callable(function_to_apply):
			raise TypeError("ERROR : First parameter is not a function")

		for i in iterable:
			yield function_to_apply(i)
	except TypeError as e:  # A non-iterable type passed as 'iterable' argument will be caught here
		sys.exit(e)


if __name__ == "__main__":
	# Example 1:
	x = [1, 2, 3, 4, 5]

	print(ft_map(lambda dum: dum + 1, x))
	# Output:
	# < generator object ft_map at 0x7f708faab7b0 >  # The address will be different

	print(list(ft_map(lambda t: t + 1, x)))
	print(list(ft_map(lambda t: t + 1, x)))
	# Output:
	# [2, 3, 4, 5, 6]
