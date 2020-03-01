# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/18 17:58:24 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/29 18:26:43 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#	Discovering how to create a class

#	Possible Improvements :
#	- Defining specific methods to handle the parsing

class Recipe:										#	Defining 'Recipe' class
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):	#	Method called when creating an object
		self.name = name							#	Attribute of class Recipe. This one stocks name for ex
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type
		try:
			assert type(name) == str and name != ""
		except AssertionError:
			print("Name should be a string and should not be empty")
			exit()
		try:
			assert type(cooking_lvl) == int and cooking_lvl > 0 and cooking_lvl < 6
		except AssertionError:
			print("Cooking level must be between 1 and 5")
			exit()
		try:
			assert type(cooking_time) == int and cooking_time > 0
		except AssertionError:
			print("cooking-time should not be negative")
			exit()
		try:
			assert type(ingredients) == list and len(ingredients) != 0
		except AssertionError:
			print("Ingredients can only be a list and must not be empty")
			exit()
		try:
			assert type(description) == str
		except AssertionError:
			print("Description should only be a string")
			exit()
		try:
			assert recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"
		except AssertionError:
			print("Wrong type of recipe")
			exit() 
	
	#	Defining a str method to print properly all information about a recipe
	def __str__(self):
		"""Return the string to print with the recipe info"""
		text = "The name of this recipe is {}, on a difficulty cooking scale up to five, it is a {}.\nIt takes {} minutes to cook.\nIt has the following ingredients : {}.\nHere is a quick description : {}.\nThis recipe is a {}.\nBon appetit !".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
		return text
		