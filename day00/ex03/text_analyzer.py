# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    text_analyzer.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/03 16:55:24 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/04 15:30:27 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer():
	printable = 0
	upper = 0
	lower = 0
	punct = 0
	spaces = 0
	i = 0
	str = sys.argv[1]
	for i in str:
		if i >= 'A' and i <= 'Z':
			upper +=1
		if i >= 'a' and i <= 'z':
			lower +=1
		if i == ' ':
			spaces +=1
		if i in string.punctuation:
			punct += 1
		if i in string.whitespace:
			spaces += 1
	print ("- ", upper,"upper letters")
	print ("- ", lower,"lower letters")
	print ("- ", spaces,"spaces")
	print ("- ", punct,"punctuations")
	print ("- ", spaces,"spaces")
text_analyzer()