# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 21:47:45 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/26 21:10:31 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
import datetime

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
			assert type(last_update) == datetime.datetime
		except AssertionError:
			print("last_update should be a datatime type")
		try:
			assert type(creation_date) == datetime.datetime
		except AssertionError:
			print("creation_date should be a datatime type")
		try:
			assert type(recipes_list) == dict
		except AssertionError:
			print("recipes_list should be a dictionnary")
	
	def get_recipes_by_type(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		recettes = self.recipes_list.get(recipe_type)
		names = []
		for i in recettes:
			names.append(i.name)
		return (names)

	# def get_recipe_by_name(self, name):
	# 	"""Print a recipe with the name 'name' and return the instance """
	# 	return (self.recipes_list.get(name))

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update """
		self.recipes_list.setdefault(recipe.recipe_type, []).append(recipe)
		# pass