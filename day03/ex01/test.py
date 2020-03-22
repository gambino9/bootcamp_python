# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamia <lamia@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/19 19:21:11 by lamia             #+#    #+#              #
#    Updated: 2020/03/22 20:29:50 by lamia            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("../42AI.png")
print(arr)
imp.display(arr)