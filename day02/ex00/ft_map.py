# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 16:10:00 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/11 17:49:27 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# The map() function applies a given function to each item of an iterable (list, 
# tuple etc.) and returns a list of the results.
# https://book.pythontips.com/en/latest/map_filter.html
# http://sametmax.com/map-filter-et-reduce/

def ft_map(function_to_apply, list_of_inputs):
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
		result.append(function_to_apply(i))
	return (result)

print("----Test Map with a tuple of numbers----")
def calculateSquare(n):
    return n*n

numbers = (1, 2, 3, 4)
result = ft_map(calculateSquare, numbers)
print(result)

print("----Test Map with a list of strings----")
def ft_upper(string):
    newstr = ""
    for c in string:
        if c.islower():
            newstr += c.upper()
        else:
            newstr += c
    return newstr

strings = "test", "str", "rokb,vfl"
result = ft_map(ft_upper, strings)
print(result)