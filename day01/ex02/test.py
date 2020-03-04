# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/01 19:02:41 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/04 21:01:19 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

liste = [0.0, 1.0, 2.0, 3.0]
range_tuple = (10, 17)
toto = Vector(liste)
# print(toto.size)
# print(toto.values)
vec1 = Vector((15, 20))
print("vec1 values", vec1.values)
vec2 = 2 * vec1
# print("vec1 values after op", vec1.values)
print("vec2 values", vec2.values)
