# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/08 18:50:43 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/08 19:11:47 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# A program to pad a string with '-' upto 42, using rjust()
# https://thispointer.com/python-how-to-pad-strings-with-zero-space-or-some-other-character/

phrase = "The right format"
padding_size = 42
res = phrase.rjust(padding_size - 1, '-')
print(res)