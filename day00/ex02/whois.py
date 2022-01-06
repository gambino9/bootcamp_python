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


def whois(number):
	if not number.isdigit():
		return "ERROR"
	else:
		num = int(number)
		if num == 0:
			return "I'm Zero."
		return "I'm Even." if num % 2 == 0 else "I'm Odd."


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("ERROR")
		sys.exit()
	print(whois(sys.argv[1]))
