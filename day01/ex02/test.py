# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/01 19:02:41 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/02 21:58:54 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

liste = [0.0, 1.0, 2.0, 3.0]
litte_tuple = (10, 17)
toto = Vector(liste)
print(toto.size)
print(toto.values)