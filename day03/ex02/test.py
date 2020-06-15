# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/25 15:36:10 by lamia             #+#    #+#              #
#    Updated: 2020/06/15 20:55:53 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from ScrapBooker import ScrapBooker

a = np.array([['A','A','A','A','A','A','A','A','A','A','A','A'],['B','B','B','B','B','B','B','B','B','B','B','B'],['C','C','C','C','C','C','C','C','C','C','C','C'], ['D','D','D','D','D','D','D','D','D','D','D','D'], ['E','E','E','E','E','E','E','E','E','E','E','E'], ['F','F','F','F','F','F','F','F','F','F','F','F'], ['G','G','G','G','G','G','G','G','G','G','G','G'], ['H','H','H','H','H','H','H','H','H','H','H','H']])
b = np.array([['A','B','C','D','E','F','G','H','I','J','K','L'],['A','B','C','D','E','F','G','H','I','J','K','L'],['A','B','C','D','E','F','G','H','I','J','K','L'], ['A','B','C','D','E','F','G','H','I','J','K','L'], ['A','B','C','D','E','F','G','H','I','J','K','L'], ['A','B','C','D','E','F','G','H','I','J','K','L'], ['A','B','C','D','E','F','G','H','I','J','K','L'], ['A','B','C','D','E','F','G','H','I','J','K','L']])

# CROP

# print (b)
# print("array shape is {}".format(b.shape))
# print("------------")
# split = 5
# train,test = b[:split,:8],b[split:,:]
# print(train)
# print(test)

# THIN

print(a)
print("array shape of a is {}".format(a.shape))
print("------------")
# a_del = np.delete(b, [:,0:10:2], 1)

# printer les rangees 
# a_del = a[::4,:]
# printer les colonnes  
# a_del = a[:,::2]
# a_del = np.delete(b, list(range(1, b.shape[0], 3)), 1)
# a_del = np.delete(b, slice(None, None, 3), 1)
a_del = np.delete(a, np.s_[3::4], 0)
print(a_del)
print("array shape of a_del is {}".format(a_del.shape))

print("------------")
a2 = np.array([[1, 2, 3],
            	[4, 5, 6],
				[7, 8, 9]])
# print(a2[])


# 3 different examples of using reshape to turn arrays into 1 2 or 3D :

# a_1d = np.arange(a,c)
# print(a_1d)

# a_2d = np.arange(12).reshape((3, 4))
# print(a_2d)

# a_3d = np.arange(24).reshape((2, 3, 4))
# print(a_3d)
