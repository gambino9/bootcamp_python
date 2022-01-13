import sys

from recipe import Recipe
import datetime


class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		try:
			if not isinstance(name, str) or not name:
				raise TypeError("ERROR : Name should be a string and should not be empty")
			self.name = name
			if not isinstance(last_update, datetime.date):
				raise TypeError("ERROR : last_update should be a datatime type")
			self.last_update = last_update
			if not isinstance(creation_date, datetime.date):
				raise TypeError("ERROR : Creation_date should be a datatime type")
			self.creation_date = creation_date
			if not isinstance(recipes_list, dict):
				raise TypeError("ERROR : Recipes_list should be a dictionary")
			if not all(key in ['starter', 'lunch', 'dessert'] for key in recipes_list.keys()):
				raise TypeError("ERROR : The dictionary does not contain the right keys")
			self.recipes_list = recipes_list

		except TypeError as te:
			sys.exit(te)

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name 'name' and return the instance"""
		try:
			if not isinstance(name, str):
				raise TypeError("ERROR : The argument must be string corresponding to a recipe name")
			recipe = None
			for key, value in self.recipes_list.items():
				for val in value:
					if val.name == name:
						recipe = val
			if not recipe:
				raise NameError("ERROR : The given name does not exist in the book")
			return recipe
		except TypeError as te:
			sys.exit(te)
		except NameError as ne:
			sys.exit(ne)

	def get_recipes_by_type(self, recipe_type):
		"""Get all recipe names for a given recipe_type and return a list"""
		try:
			if not isinstance(recipe_type, str) or recipe_type not in self.recipes_list:
				raise TypeError("ERROR : The arg must be an existing type of recipe from the book")
			names_list = [recette.name for recette in self.recipes_list[recipe_type]]
			return names_list
		except TypeError as te:
			sys.exit(te)

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update """
		try:
			if not isinstance(recipe, Recipe):
				raise TypeError("ERROR : The argument must be a Recipe object")
			type = recipe.recipe_type
			self.recipes_list[type].add(recipe)
			self.last_update = datetime.datetime.now()
		except TypeError as te:
			sys.exit(te)

	def print_content_recipe_list(self):
		for key, value in self.recipes_list.items():
			print(f"{key} contains : ")
			for i in value:
				print(i.name)
