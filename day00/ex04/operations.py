# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/04 15:29:57 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/07 17:00:11 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

# class InputError(Error):
# 	"""Exception raised for errors in the input
# 	"""

#	Proposition d'amelioration:
#
#	Utiliser des classes (ou autre) pour automatiser les cas d'erreurs	
#	Executer la fonction autrement qu'en l'appelant en fin de fichier ?

def	operations():
	if len(sys.argv) < 3:
		print("Usage : python operation.py\nExample :\n\tpython operations.py 10 3")
	elif len(sys.argv) == 3:
		try:
			a, b = int(sys.argv[1]), int(sys.argv[2]) 
		except ValueError:
			print("InputError : Only numbers\n\nUsage : python operation.py\nExample :\n\tpython operations.py 10 3")
			exit()
		print("Sum		:", a + b)
		print("Difference	:", a - b)
		print("Product		:", a * b)
		try:
			print("Quotient	:", a / b)
			print("Remainder	:", a % b)
		except ZeroDivisionError:
			print("Quotient 	: ERROR (div by zero)")
			print("Remainder 	: ERROR (div by zero)")
	elif len(sys.argv) > 3:
		print("InputError : Too many arguments\n\nUsage : python operation.py\nExample :\n\tpython operations.py 10 3")

operations()
