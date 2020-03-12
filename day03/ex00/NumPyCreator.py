# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 18:48:01 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/12 19:52:28 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://stackoverflow.com/questions/26850355/converting-list-to-numpy-array
# https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randint.html

import numpy as np

class NumPyCreator():
	def __init__(self):
		pass

	def from_list(self, lst):
		return (np.asarray(lst))
	
	def from_tuple(self, tpl):
		return (np.asarray(tpl))

	def from_iterable(self, itr):
		return (np.fromiter(itr, int))
	
	def from_shape(self, shape, value=0):
		return (np.full(shape, value))

	def random(self, shape):
		return(np.random.random(shape))
	
	def identity(self, n):
		return (np.identity(n))
	
# Turns a list into an array
npc = NumPyCreator()
print(type(npc.from_list([[1,2,3],[6,3,4]])))
print("-----------")

# Turns a tuple into an array
tup = (3, 5, 7)
print(type(tup))
print(type(npc.from_tuple(tup)))
print("-----------")

# Turns a iterable into an array
it = (x*x for x in range(5))
print(type(it))
print(type(npc.from_iterable(it)))
print("-----------")

# Returns an array filled with random values
shap = (5, 3)
print(npc.random(shap))
print("-----------")

# Returns an array filled with the same value
shap = (5, 3)
print(npc.from_shape(shap))
print("-----------")

# Returns an array representing the identity matrix of size n
n = 4
print(npc.identity(n))
print("-----------")