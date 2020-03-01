# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/01 19:02:39 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/01 20:40:56 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
	def __init__(self, values, size):
		self.values = values	# list of floats
		self.size = size		# size of vector (nb of elem)
		try:
			assert type(values) == list and len(values) != 0
		except AssertionError:
			print("Values must be a list of floats")
			exit()
		for i in values:
			if (type(i) != float):
				print("List must contain floats only")
				exit()

# liste = [0.0, 1.0, 2.0, 3.0]
# toto = Vector(liste, 4)
# print(toto.values)

titi = Vector([0.1, 1.1, 2.1], 3)
# print(titi.values)