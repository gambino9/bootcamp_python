import numpy as np
from ScrapBooker import ScrapBooker

a = np.array([['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
			  ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
			  ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
			  ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
			  ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
			  ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
			  ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
			  ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']])

b = np.array([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
			  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
			  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
			  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
			  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
			  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
			  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
			  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']])

# # CROP
# print(b)
# pos = (2, 2)
# dimension = (1, 5)
# c = b[pos[0]:(pos[0] + dimension[0]), pos[1]:(pos[1] + dimension[1])]
# print(c)
# print(c.shape)

spb = ScrapBooker()
# print(arr1 := np.arange(0,25).reshape(5,5))
# print(spb.crop(arr1, (3,1),(1,0)))
# # Output
# # array([[ 5],
# # 	   [10],
# # 	   [15]])

# THIN

# print(a)
# print("array shape of a is {}".format(a.shape))
# print("------------")
# a_del = np.delete(a, np.s_[3::4], 1)
# print(a_del)
# print("array shape of a_del is {}".format(a_del.shape))
# print("------------")

# print(arr2 := np.array("A B C D E F G H I".split() * 6).reshape(-1,9))
# print(spb.thin(arr2,3,0))
# print(spb.thin(arr2,3,0).dtype)
# # Output :
# # array([['A', 'B', 'D', 'E', 'G', 'H'],
# # 	   ['A', 'B', 'D', 'E', 'G', 'H'],
# # 	   ['A', 'B', 'D', 'E', 'G', 'H'],
# # 	   ['A', 'B', 'D', 'E', 'G', 'H'],
# # 	   ['A', 'B', 'D', 'E', 'G', 'H'],
# # 	   ['A', 'B', 'D', 'E', 'G', 'H']], dtype='<U1')

# print(arr3 := np.array([[var] * 10 for var in "ABCDEFG"]))
# print(spb.thin(arr3,3,1))
# print(spb.thin(arr3,3,1).dtype)
#
# # Output :
# # array([['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
# # 	   ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
# # 	   ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
# # 	   ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
# # 	   ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']], dtype='<U1')

# JUXTAPOSE & MOSAIC

# a1 = np.array([[1, 2, 3],
# 				[4, 5, 6],
# 				[7, 8, 9]])
# n = 3
# print(a1)
# print("------------")
# # a2 = np.concatenate([a1] * n,0)
# a2 = np.tile(a1, (4, 3))
# print("------------")
# # a2 = np.tile(a1,2)
# print(a2)

print(arr4 := np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
print(spb.juxtapose(arr4, 2, 0))

# Output :
# array([[1, 2, 3],
# 	   [4, 5, 6],
# 	   [7, 8, 9],
# 	   [1, 2, 3],
# 	   [4, 5, 6],
# 	   [7, 8, 9]])

# 3 different examples of using reshape to turn arrays into 1 2 or 3D :

# a_1d = np.arange(a,c)
# print(a_1d)

# a_2d = np.arange(12).reshape((3, 4))
# print(a_2d)

# a_3d = np.arange(24).reshape((2, 3, 4))
# print(a_3d)
