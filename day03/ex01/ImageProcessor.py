# https://stackoverflow.com/questions/20597088/display-a-png-image-from-python-on-mint-15-linux
# http://www.degeneratestate.org/posts/2016/Oct/23/image-processing-with-numpy/

import matplotlib.pyplot as plt


class ImageProcessor():
	def __init__(self):
		pass

	def load(self, path):
		""" opens the .png file specified by the path argument and returns 
		an array with the RGB values of the image pixels.
		It must display a message specifying the dimensions of the image
		(e.g. 340 x 500)""" 
		img = plt.imread(path)
		y = img.shape[0]
		x = img.shape[1]
		print(f"Loading image of dimensions {x} x {y}")
		return img

	def display(self, array):
		plt.imshow(array)
		plt.show() 
