# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 19:44:24 by lboukrou          #+#    #+#              #
#    Updated: 2020/01/13 20:22:54 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def whois():
	x = 0
	if (len(sys.argv) != 2):
		return ("ERROR")
	if (sys.argv[1].isdigit() == False):
		return ("ERROR")
	x = int(sys.argv[1])
	if (x == 0):
		return  ("I'm Zero.")
	elif (x % 2 == 0):
		return  ("I'm Even.")
	elif (x % 2 != 0):
		return  ("I'm Odd.")
	else:
		return  ("ERROR")

print (whois())
