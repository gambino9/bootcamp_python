# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/01 19:02:39 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/02 21:59:48 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
	def __init__(self, values=None):
		# self.values = values	# list of floats
		# self.size = None		# size of vector (nb of elem)
		if values != None:
			if type(values) == list:
				for i in values:
					if (type(i) != float):
						print("List must contain floats only")
						exit()
				self.values = values
				self.size = len(values)
			elif type(values) == int:
				self.size = values
				init = float(0.0)
				float_list = []
				for i in range(0, self.size):
					float_list.append(float(i))
				self.values = float_list
			elif type(values) == tuple and len(values) == 2:
				float_list = [i * 1.0 for i in range(values[0], values[1])]
				self.values = float_list
				self.size = len(self.values)
		elif values == None:
			print("Please enter a value")
			exit()
		
		# elif values != None and type(values) == list and size == None:
		# 	for i in values:
		# 		if (type(i) != float):
		# 			print("List must contain floats only")
		# 			exit()
		# 		else:
		# 			print("ouhlala")
		# 	# put something
		# elif size != None and values == None:
		# 	init = float(0.0)
		# 	float_list = []
		# 	for i in range(0, size):
		# 		float_list.append(init + (float(i) / 100))
		# 	self.values = float_list
		# else:
		# 	print("coucou")

		# elif

	# def init_by_list(self, values):


# liste = [0.0, 1.0, 2.0, 3.0]
# toto = Vector(liste, 4)
# print(toto.values)

# titi = Vector([0.1, 1.1, 2.1], 3)
# print(titi.values)