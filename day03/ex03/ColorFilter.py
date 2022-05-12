# https://yashaslokesh.github.io/inverting-the-colors-of-an-image.html

import numpy as np


class ColorFilter:
	def __init__(self):
		pass

	def invert(self, array):
		"""
		Inverts the color of the image received as a numpy array.
		Args:
		array: numpy.ndarray corresponding to the image.
		Return:
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		This function should not raise any Exception.
		"""
		colors_arr = array[:, :, :3]  # Takes color data from image array, without last channel
		invert_col_arr = 1 - colors_arr

		return invert_col_arr

	def to_blue(self, array):
		"""
		Applies a blue filter to the image received as a numpy array.
		Args:
		array: numpy.ndarray corresponding to the image.
		Return:
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		This function should not raise any Exception.
		◦ Authorized functions:.zeros,.shape,.dstack
		◦ Authorized operator:None
		"""
		colors_arr = np.zeros((len(array), len(array[0]), 3))
		colors_arr[:,:,2] = array[:, :, 2]

		return colors_arr

	def to_green(self, array):
		"""
		Applies a green filter to the image received as a numpy array.
		Args:
		array: numpy.ndarray corresponding to the image.
		Return:
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		This function should not raise any Exception.
		"""
		colors_arr = np.zeros((len(array), len(array[0]), 3))
		colors_arr[:,:,1] = array[:, :, 1]

		return colors_arr

	def to_red(self, array):
		"""
		Applies a red filter to the image received as a numpy array.
		Args:
		array: numpy.ndarray corresponding to the image.
		Return:
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		This function should not raise any Exception.
		"""
		colors_arr = np.zeros((len(array), len(array[0]), 3))
		colors_arr[:,:,0] = array[:, :, 0]

		return colors_arr

	def celluloid(self, array):
		"""
		Applies a celluloid filter to the image received as a numpy array.
		Celluloid filter must display at least four thresholds of shades.
		Be careful! You are not asked to apply black contour on the object,
		you only have to work on the shades of your images.
		Remarks:
		celluloid filter is also known as cel-shading or toon-shading.
		Args:
		array: numpy.ndarray corresponding to the image.
		Return:
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		This function should not raise any Exception.
		"""

	def to_grayscale(self, array, filter, **kwargs):
		"""
		Applies a grayscale filter to the image received as a numpy array.
		For filter = ’mean’/’m’: performs the mean of RBG channels.
		For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
		Args:
		array: numpy.ndarray corresponding to the image.
		filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
		weights: [kwargs] list of 3 floats where the sum equals to 1,
		corresponding to the weights of each RBG channels.
		Return:
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		This function should not raise any Exception.
		"""
		if filter not in ['m', 'mean', 'w', 'weight']:
			return None

		# We iterate through every row of the np array and replace the 3 RGB
		# with the calculated mean of the 3 RGB channels
		if filter in ['mean', 'm']:
			for color_array in array:
				for rgb in color_array:
					rgb[..., :3] = np.mean(rgb[..., :3])
			return array
		# We iterate through every row of the np array and replace the 3 RGB
		# with the calculated dot product between the RGB value and the weight
		elif filter in ['weighted', 'w']:
			for color_array in array:
				for rgb in color_array:
					rgb[..., :3] = np.dot(rgb[..., :3], kwargs.get('weight'))
			return array
