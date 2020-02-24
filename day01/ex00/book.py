# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 21:47:45 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/24 21:59:33 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		self.name = name
		self.last_update = last_update
		self.creation_date = creation_date
		self.recipes_list = recipes_list
		try:
			assert type(name) == str and name != ""
		except AssertionError:
			print("Name should be a string and should not be empty")
			exit()
		try:
			