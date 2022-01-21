# Reduce is a really useful function for performing some computation on a list
# and returning the result. It applies a rolling computation to sequential pairs
# of values in a list. For example, if you wanted to compute the product of a 
# list of integers.

def ft_reduce(function_to_apply, list_of_inputs):
	try:
		assert callable(function_to_apply)
		assert list_of_inputs != None
		iter(list_of_inputs)
		list_len = len(list_of_inputs)
		res = list_of_inputs[0]
		for i in range(1, list_len):
			res = function_to_apply(res, list_of_inputs[i])
		return res
	except:
		print("Error")
		
print("----Test Map with a tuple of numbers----")
def prout(nb1, nb2):
	return nb1 + nb2
numbers = (1, 2, 3, 4)
result = ft_reduce(prout, numbers)
print(result)