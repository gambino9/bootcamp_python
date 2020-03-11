# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 15:23:06 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/11 12:37:19 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Matrix has 2 attributes : 
# 	- data (list of lists of elements stored in the matrix)
#	- shape, a Tuple containing dimensions (row, columns)
#
# We should be able to initialize th object with : 
# 	1 - the elements of the matrix as a list of lists (data) : 
# Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])-> the dimensions of this 
# matrix are then (2, 4)
# 	2 - a shape Matrix((3, 3))-> the matrix will be filled by default with zeroes
# 	3 - the expected elements and shape : Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], 
# [6.0, 7.0, 8.0]],(3, 3))

class Matrix:
	def __init__ (self, *data):
		# """ 1 """
		if len(data) == 1:
			if type(data[0]) == list:
				length = len(data[0][0])
				for i in data[0]:
					if type(i) != list:
						print("data must only contain lists")
						exit()
					if len(i) != length:
						print("data's lists must be of same length")
						exit()
				self.data = data[0]
				self.shape = (len(self.data), length)
				# self.shape[0] = len(self.data[0])
				# self.shape[1] = length
		# """ 2 """ 
			elif type(data[0]) == tuple:
				if (len(data[0]) != 2):
					print("Shape must contains 2 elements")
					exit()
				self.shape = data
				num_list = self.shape[0]
				num_elem = self.shape[1]
				print(num_list)
				self.data = []
				for i in range (num_list):
					col = []
					for j in range (num_elem):
						col.append()
					self.data.append(col)
		# """ 3 """
		elif len(data) == 2:
			if type(data[0]) == list and type(data[1]) == tuple:
				self.data = data[0]
				self.shape = data[1]
			else:
				print("Wrong type of elements")
				exit()
		elif len(data) == 0:
			print("Please enter arguments")
			exit()
		else:
			print("Wrong number of arguments")
			exit()

					


				

				


     
	