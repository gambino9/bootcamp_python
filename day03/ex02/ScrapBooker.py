# https://www.tutorialspoint.com/numpy/numpy_indexing_and_slicing.htm
# https://note.nkmk.me/en/python-numpy-ndarray-ndim-shape-size
# https://machinelearningmastery.com/index-slice-reshape-numpy-arrays-machine-learning-python/
# https://www.pythoninformer.com/python-libraries/numpy/index-and-slice/
# https://note.nkmk.me/en/python-numpy-delete/
# https://numpy.org/doc/1.18/reference/generated/numpy.concatenate.html
# https://numpy.org/doc/stable/reference/generated/numpy.tile.html

import sys

import numpy as np


class ScrapBooker:
	def __init__(self):
		pass

	def crop(self, array, dim, position=(0, 0)):
		""" crop the image as a rectangle with the given dimensions
		(meaning, the new height and width for the image), whose top left
		corner is given by the position argument.
		The position should be (0,0) by default. You have to consider it an
		error (and handle said error) if dimensions is larger than the current
		image size."""
		try:
			if not all(isinstance(arg, tuple) for arg in [dim, position]):
				raise TypeError("Dimensions and position must be tuples")
			if any(i < 0 for i in dim) or any(j < 0 for j in position):
				raise TypeError("Dimensions and position must not be negative numbers")
			if not all(x > y for x, y in zip(array.shape, dim)):
				raise TypeError("Dimensions must be inferior to array's dimensions")
			row = dim[0]
			column = dim[1]
			arr = np.array(array)
			new_array = arr[position[0]:(position[0] + row), position[1]:(position[1] + column)]
			return new_array
		except TypeError as e:
			sys.exit(e)

	def thin(self, array, n, axis):  # TODO : Seems to work, gotta check though
		""" delete every n-th pixel row along the specified axis
		(0 vertical, 1 horizontal)."""
		axis = 1 - axis
		arr = np.delete(array, np.s_[n-1::n], axis)
		return arr

	def juxtapose(self, array, n, axis):  # TODO : This one gotta be checked, does not work properly
		""" juxtapose n copies of the image along the specified axis
		(0 vertical, 1 horizontal)"""
		axis = 1 - axis
		return np.concatenate([array] * n, axis)

	def mosaic(self, array, dim):
		""" make a grid with multiple copies of the array.
		The dimensions argument specifies the dimensions (meaning
		the height and width) of the grid (e.g. 2x3)."""
		return np.tile(array, dim)
