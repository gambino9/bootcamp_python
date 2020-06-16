# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/23 15:54:49 by lamia             #+#    #+#              #
#    Updated: 2020/06/16 20:25:32 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://www.tutorialspoint.com/numpy/numpy_indexing_and_slicing.htm
# https://note.nkmk.me/en/python-numpy-ndarray-ndim-shape-size
# https://machinelearningmastery.com/index-slice-reshape-numpy-arrays-machine-learning-python/
# https://www.pythoninformer.com/python-libraries/numpy/index-and-slice/
# https://note.nkmk.me/en/python-numpy-delete/
# https://numpy.org/doc/1.18/reference/generated/numpy.concatenate.html
# https://numpy.org/doc/stable/reference/generated/numpy.tile.html

import numpy as np

class ScrapBooker():
    def __init__(self):
        pass
    
    def crop(self, array, dimensions, position):
        """ crop the image as a rectangle with the given dimensions
        (meaning, the new height and width for the image), whose top left
        corner is given by the position argument.
        The position should be (0,0) by default. You have to consider it an
        error (and handle said error) if dimensions is larger than the current
        image size."""
        try:
            if dimensions > array.shape:
                raise TypeError("dimensions must be inferior to array's dimensions")
        except TypeError as e:
            print(e)
            exit()
        height = dimensions[0]
        width = dimensions[1]
        arr = np.array(array)
        newArr = arr[:height,width]
        return (newArr)

    def thin(self, array, n, axis):
        """ delete every n-th pixel row along the specified axis
        (0 vertical, 1 horizontal)."""
        axis = 1 - axis
        arr = np.delete(array, np.s_[n-1::n], axis)
        return (arr)

    def juxtapose(self, array, n, axis):
        """ juxtapose n copies of the image along the specified axis
        (0 vertical, 1 horizontal)""" 
        axis = 1 - axis
        return (np.concatenate([array] * n, axis))

    def mosaic(self, array, dimensions):
        """ make a grid with multiple copies of the array.
        The dimensions argument specifies the dimensions (meaning
        the height and width) of the grid (e.g. 2x3)."""
        return (np.tile(array, (dimensions)))