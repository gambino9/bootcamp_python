def ft_filter(function_to_apply, iterable):
	"""
		Filter the result of function apply to all elements of the iterable.
		Args:
		function_to_apply: a function taking an iterable.
		iterable: an iterable object (list, tuple, iterator).
		Returns:
		An iterable.
		None if the iterable can not be used by the function.
	"""
	try:
		if not callable(function_to_apply):
			raise TypeError("First parameter is not a function")

		for i in iterable:
			if function_to_apply(i):
				yield i
	except TypeError as e:
		exit(e)


if __name__ == "__main__":
	x = [1, 2, 3, 4, 5]

	print(ft_filter(lambda dum: not (dum % 2), 9))
	# Output:
	# < generator object ft_filter at 0x7f709c777d00 >  # The adress will be different

	print(list(ft_filter(lambda dum: not (dum % 2), x)))
	# Output:
	# [2, 4]
