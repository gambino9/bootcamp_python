# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamia <lamia@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/23 15:54:49 by lamia             #+#    #+#              #
#    Updated: 2020/03/23 22:54:35 by lamia            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://www.tutorialspoint.com/numpy/numpy_indexing_and_slicing.htm

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
        pass

    def thin(self, array, n, axis):
        """ delete every n-th pixel row along the specified axis
        (0 vertical, 1 horizontal), example below.""" 
        pass

    def juxtapose(self, array, n, axis):
        """ juxtapose n copies of the image along the specified axis
        (0 vertical, 1 horizontal)""" 
        pass

    def mosaic(self, array, dimensions):
        """ make a grid with multiple copies of the array.
        The dimensions argument specifies the dimensions (meaning
        the height and width) of the grid (e.g. 2x3).""" 
        pass