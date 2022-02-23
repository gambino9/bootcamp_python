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
		"""
		Crops the image as a rectangle via dim arguments (being the new height
		and width of the image) from the coordinates given by position arguments.
		Args:
		array: numpy.ndarray
		dim: tuple of 2 integers.
		position: tuple of 2 integers.
		Returns:
		new_arr: the cropped numpy.ndarray.
		None otherwise (combination of parameters not incompatible).
		Raises:
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray):
			return None
		if not all(isinstance(arg, tuple) for arg in [dim, position]):
			return None
		if any(i < 0 for i in dim) or any(j < 0 for j in position):
			return None
		if len(dim) != 2 or len(position) != 2:
			return None
		if not all(x > y for x, y in zip(array.shape, dim)):
			return None
		row = dim[0]
		column = dim[1]
		arr = np.array(array)
		new_array = arr[position[0]:(position[0] + row), position[1]:(position[1] + column)]
		return new_array

	def thin(self, array, n, axis):
		"""
		Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
		Args:
		array: numpy.ndarray.
		n: non-null positive integer lower than the number of row/column of the array
		(depending on axis value).
		axis: positive non-null integer.
		Returns:
		new_arr: thinned numpy.ndarray.
		None otherwise (combination of parameters not incompatible).
		Raises:
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray):
			return None
		if n < 0 or not (0 <= axis <= 1):
			return None
		axis = 1 - axis
		arr = np.delete(array, np.s_[n-1::n], axis)
		return arr

	def juxtapose(self, array, n, axis):
		"""
		Juxtaposes n copies of the image along the specified axis.
		Args:
		array: numpy.ndarray.
		n: positive non-null integer.
		axis: integer of value 0 or 1.
		Returns:
		new_arr: juxtaposed numpy.ndarray.
		None otherwise (combination of parameters not incompatible).
		Raises:
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray):
			return None
		if n < 0 or not (0 <= axis <= 1):
			return None
		return np.concatenate([array] * n, axis)

	def mosaic(self, array, dim):
		"""
		Makes a grid with multiple copies of the array. The dim argument
		specifies the number of repetition along each dimensions.
		Args:
		array: numpy.ndarray.
		dim: tuple of 2 integers.
		Returns:
		new_arr: mosaic numpy.ndarray.
		None otherwise (combination of parameters not incompatible).
		Raises:
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray):
			return None
		if len(dim) != 2 or any(i < 0 for i in dim):
			return None
		return np.tile(array, dim)
