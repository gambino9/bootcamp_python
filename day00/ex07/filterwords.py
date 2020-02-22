# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/13 19:31:24 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/22 17:52:57 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#	Discovering list comprehensions
#	Note : Have to manage parse of string argument

import string
import sys

def filterwords():
	if len(sys.argv) != 3:
		print("ERROR")
		exit()
	try:
		c = str(sys.argv[1])
		n = int(sys.argv[2])
	except ValueError:
		print("ERROR")
		exit()
	no_punct = ""
	for char in c:
		if char not in string.punctuation:
			no_punct = no_punct + char

	hello = no_punct.split()
	lst = []
	for word in no_punct.split():
		if len(word) <= n:
			continue
		else:
			lst.append(word)
	print(lst)

filterwords()


