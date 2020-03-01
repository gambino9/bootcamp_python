# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/29 18:28:43 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/01 19:01:15 by lboukrou         ###   ########.fr        #
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
		""" Family of bad guys"""
		super().__init__(first_name=first_name, is_alive=is_alive)	# super() calls the parent class
		self.family_name = "Lannister"
		self.house_words = "Sorry, didn't watch the show"
	
# Method to child class : print house words
	def print_house_words(self):
		print(self.house_words)

# Method to child class : change value of is_alive to False
	def die(self):
		self.is_alive=False

#Creating object Arya of type Lannister
arya = Lannister("Arya")
print(arya.first_name)
print(arya.is_alive)
arya.print_house_words()
arya.die()
print(arya.is_alive)
