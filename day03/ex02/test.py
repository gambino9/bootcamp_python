# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/25 15:36:10 by lamia             #+#    #+#              #
#    Updated: 2020/06/08 20:54:16 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from ScrapBooker import ScrapBooker

a = np.array([['A','A','A','A','A','A','A','A','A','A','A','A'],['B','B','B','B','B','B','B','B','B','B','B','B'],['C','C','C','C','C','C','C','C','C','C','C','C'], ['D','D','D','D','D','D','D','D','D','D','D','D'], ['E','E','E','E','E','E','E','E','E','E','E','E'], ['F','F','F','F','F','F','F','F','F','F','F','F'], ['G','G','G','G','G','G','G','G','G','G','G','G'], ['H','H','H','H','H','H','H','H','H','H','H','H']])
print (a)
print("------------")
# print(a.shape)
# print(a[0,])
X, y = a[:, :-1], a[:, -1]
print(X)
print("------------")
print(y)
# b = a[...,2]
# c = a[2,...]
# d = a[...,1:]
# e = a[4:]
# print("--------")
# print(b)
# print("--------")
# print(c)
# print("--------")
# print(d)
# print("--------")
# print(e)

# 3 different examples of using reshape to turn arrays into 1 2 or 3D :

# a_1d = np.arange(a,c)
# print(a_1d)

# a_2d = np.arange(12).reshape((3, 4))
# print(a_2d)

# a_3d = np.arange(24).reshape((2, 3, 4))
# print(a_3d)
