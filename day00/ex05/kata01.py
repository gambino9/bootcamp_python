# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/07 18:05:50 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/07 18:42:03 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Introduction to dictionnaries in Python
# https://www.w3schools.com/python/python_dictionaries.asp
# A simple exercice to print keys and keys's values

languages = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

for i in languages:
	print(i,"was created by",languages[i])