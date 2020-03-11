# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 16:46:44 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/11 12:39:09 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from matrix import Matrix

liste = ([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]])
print(type(liste))
print("------")
data = []
num_list= 3
num_elem= 4
for i in range (num_list):
	col = []
	for j in range (num_elem):
		col.append(0.0)
	data.append(col)
print(data)
print("------")
# for i in liste:
# 	print(type(i))
# print(len(liste))
# print("------")
# print(len(liste[0]))
# print("------")
# tutu = ()
# tutu = (0, 1, 45)
# print(type(tutu))
# print(len(tutu))
# print(tutu[2])
# print("------")
# lolo = [[]]
# print(type(lolo))
# print(len(lolo))

m1 = Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0], [9.0, 10.0, 11.0]])
print(m1.shape)
print(m1.data)
# m2 = Matrix()
