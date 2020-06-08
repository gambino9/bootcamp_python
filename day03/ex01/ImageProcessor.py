
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 19:55:19 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/12 20:10:52 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://stackoverflow.com/questions/20597088/display-a-png-image-from-python-on-mint-15-linux
# http://www.degeneratestate.org/posts/2016/Oct/23/image-processing-with-numpy/

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
		print("Loading image of dimensions {} x {}".format(x, y))
		# print(y)
		# print(x)
		return (img)
		

	def display(self, array):
		plt.imshow(array)
		plt.show() 
		pass
