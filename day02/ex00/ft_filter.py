# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 17:29:50 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/11 17:45:49 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# As the name suggests, filter creates a list of elements for which a function
# returns true.

def ft_filter(function_to_apply, list_of_inputs):
	try:
		if not list_of_inputs:
			raise TypeError("ft_map should at least have two parameters")
		if not callable(function_to_apply):
			raise TypeError("First parameter is not a function")
	except TypeError as e:
		print(e)
		exit()
	result = []
	for i in list_of_inputs:
		if function_to_apply(i) == True:
			result.append(i)
	return (result)

print("----Test Map with a tuple of numbers----")
def CheckNumbers(n):
	if n % 2:
		return True
	else:
		return False

numbers = (1, 2, 3, 4)
result = ft_filter(CheckNumbers, numbers)
print(result)