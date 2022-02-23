import numpy as np
from ScrapBooker import ScrapBooker

###############################################################################
# TESTS FROM SUBJECT

# # Test 1
spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))
# #Output
# # array([[ 5],
# # 	   [10],
# # 	   [15]])
#
#
# # Test 2 (from 42AI slack example (the second example from subject is false))
arr2 = np.array("A B C D E F G H I J Q L".split() * 6).reshape(-1,12)
tp_np_array = np.array("A B C D E F G H I J K L".split())
arr3 = np.transpose([tp_np_array] * 12)
print(spb.thin(arr2,3,0))
# Output :
# # perform thin with n=3 and axis=0:
# # 	ABCDEFGHIJQL        ABDEGHJQ
# # ABCDEFGHIJQL        ABDEGHJQ
# # ABCDEFGHIJQL        ABDEGHJQ
# # ABCDEFGHIJQL        ABDEGHJQ
# # ABCDEFGHIJQL        ABDEGHJQ
# # ABCDEFGHIJQL  ==>   ABDEGHJQ
# # ABCDEFGHIJQL        ABDEGHJQ
# # ABCDEFGHIJQL        ABDEGHJQ
# # ABCDEFGHIJQL        ABDEGHJQ
# # ABCDEFGHIJQL        ABDEGHJQ
# # ABCDEFGHIJQL        ABDEGHJQ
# #
print(spb.thin(arr3,4,1))
# Output
# # perform thin with n=4 and axis=1:
# # 	AAAAAAAAAAAA
# # BBBBBBBBBBBB        AAAAAAAAAAAA
# # CCCCCCCCCCCC        BBBBBBBBBBBB
# # DDDDDDDDDDDD        CCCCCCCCCCCC
# # EEEEEEEEEEEE        EEEEEEEEEEEE
# # FFFFFFFFFFFF  ==>   FFFFFFFFFFFF
# # GGGGGGGGGGGG        GGGGGGGGGGGG
# # HHHHHHHHHHHH        IIIIIIIIIIII
# # IIIIIIIIIIII        JJJJJJJJJJJJ
# # JJJJJJJJJJJJ        KKKKKKKKKKKK
# # KKKKKKKKKKKK
# # LLLLLLLLLLLL

# Test 3
arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))
#Output
# array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
# 	   [1, 2, 3, 1, 2, 3, 1, 2, 3],
# 	   [1, 2, 3, 1, 2, 3, 1, 2, 3]])


###############################################################################
# TESTS FROM CORRECTION :

spb = ScrapBooker()

# Test 1
print(arr2 := np.array("A B C D E F G H I".split() * 6).reshape(-1,9))
print(spb.thin(arr2,3,0))
print(spb.thin(arr2,3,0).dtype)

# Output :
# array([['A', 'B', 'D', 'E', 'G', 'H'],
# 	   ['A', 'B', 'D', 'E', 'G', 'H'],
# 	   ['A', 'B', 'D', 'E', 'G', 'H'],
# 	   ['A', 'B', 'D', 'E', 'G', 'H'],
# 	   ['A', 'B', 'D', 'E', 'G', 'H'],
# 	   ['A', 'B', 'D', 'E', 'G', 'H']], dtype='<U1')

# Test 2
print(arr3 := np.array([[var] * 10 for var in "ABCDEFG"]))
print(spb.thin(arr3,3,1))
print(spb.thin(arr3,3,1).dtype)

# Output:
# array([['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
# 	   ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
# 	   ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
# 	   ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
# 	   ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']], dtype='<U1')

# Test 3
print(arr4 := np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
print(spb.juxtapose(arr4, 2, 0))

# Output :
# array([[1, 2, 3],
# 	   [4, 5, 6],
# 	   [7, 8, 9],
# 	   [1, 2, 3],
# 	   [4, 5, 6],
# 	   [7, 8, 9]])

# Test 4
# ERROR MANAGEMENT
print(not_numpy_arr := [[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(spb.crop(not_numpy_arr, (1,2)))
print(spb.juxtapose(arr4, -2, 0))
print(spb.mosaic(arr4, (1, 2, 3)))

# Output :
# These functions should all return None because of incorrect parameters
