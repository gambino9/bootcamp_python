# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/08 19:12:02 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/11 17:33:49 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Way of writing number in scientific notation :
# print(format(tup[3], "1.2e"))
# print(format(tup[4], "1.2e"))

tup = (0, 4, 132.42222, 10000, 12345.67)

print("day_0%d, ex_0%d : %.2f," % (tup[0], tup[1], tup[2]), format(tup[3], "1.2e"), ",", format(tup[4], "1.2e"))
