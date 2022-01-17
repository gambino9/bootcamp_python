# https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/

import random


def shuffle(arr):
	n = len(arr)

	# repeat the following for n number of times
	for i in range(n):
		# select an index randomly
		j = random.randint(0, n - 1)
		# delete the element at that index.
		element = arr.pop(j)
		# now append that deleted element to the list
		arr.append(element)
	return arr


def generator(text, sep=" ", option=None):
	opt = ['shuffle', 'unique', 'ordered', None]
	try:
		if option not in opt or not isinstance(text, str):
			raise ValueError("ERROR")
		arr = text.split(sep)
		new_arr = arr
		if option == 'shuffle':
			new_arr = shuffle(arr)
		elif option == 'unique':
			new_arr = list(set(arr))
		elif option == 'ordered':
			new_arr = sorted(arr)
		for word in new_arr:
			yield word
	except ValueError as ve:
		exit(ve)


def test_generator_function(text, option=None):
	for word in generator(text, option=option):
		print(word)


if __name__ == "__main__":
	# Tests
	lorem_text = "Le Lorem Ipsum est simplement du faux texte."
	test_generator_function(lorem_text)
	# test_generator_function(lorem_text, 'shuffle')
	# test_generator_function(lorem_text, 'unique')
	# test_generator_function(lorem_text, 'ordered')

