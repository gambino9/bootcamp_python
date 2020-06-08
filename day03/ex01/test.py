# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/19 19:21:11 by lamia             #+#    #+#              #
#    Updated: 2020/06/08 18:22:18 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("../42AI.png")
print(arr)
# imp.display(arr)