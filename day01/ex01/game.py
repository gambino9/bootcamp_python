# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/29 18:28:43 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/29 20:59:47 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Seing some more classes
# Discovering inheritance

class GotCharacter:
	def __init__(self, first_name, is_alive=True):
		self.first_name = first_name
		self.is_alive = is_alive

class Lannister(GotCharacter):
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)	# super() calls the parent class
		self.family_name = "Lannister"
		self.house_words = "Sorry, didn't watch the show"
	
# Method to child class : print house words
	def print_house_words(self, house_words):
		print(house_words)

lolo = print_house_words()


# Method to child class : change value of is_alive to False

lol = GotCharacter("lolilol")
# lol.first_name = lolilol
# lol.is_alive = True
print(lol.first_name)
print(lol.is_alive)
