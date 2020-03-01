# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/01 19:02:41 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/01 20:37:47 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

liste = [0.0, 1.0, 2.0, 3.0]
toto = Vector(liste, 4)
print(toto.size)
print(toto.values)