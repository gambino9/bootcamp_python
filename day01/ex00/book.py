import sys

from recipe import Recipe
import datetime


class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		try:
			if not isinstance(name, str) or not name:
				raise TypeError("Name should be a string and should not be empty")
			self.name = name
			if not isinstance(last_update, datetime.date):
				raise TypeError("last_update should be a datatime type")
			self.last_update = last_update
			if not isinstance(creation_date, datetime.date):
				raise TypeError("creation_date should be a datatime type")
			self.creation_date = creation_date
			if not isinstance(recipes_list, dict):
				raise TypeError("recipes_list should be a dictionary")
			if not all(key in ['starter', 'lunch', 'dessert'] for key in recipes_list.keys()):
				raise TypeError("The dictionary does not contain the right keys")
			self.recipes_list = recipes_list

		except TypeError as te:
			sys.exit(te)

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name 'name' and return the instance"""
		try:
			if not isinstance(name, str):
				raise TypeError("The argument must be string corresponding to a recipe name")
			recipe = None
			for key, value in self.recipes_list.items():
				for val in value:
					if val.name == name:
						recipe = val
			if not recipe:
				raise NameError("The given name does not exist in the book")
			return recipe
		except TypeError as te:
			sys.exit(te)
		except NameError as ne:
			sys.exit(ne)

	def get_recipes_by_type(self, recipe_type):
		"""Get all recipe names for a given recipe_type and return a list"""
		if isinstance(recipe_type, str) and recipe_type in self.recipes_list:
			names_list = [recette.name for recette in self.recipes_list[recipe_type]]
			return names_list
		else:
			return "The argument must be a existing type of recipe from the recipe_list dict"

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update """
		if not isinstance(recipe, Recipe):
			raise TypeError("The argument must be a Recipe object")
		type = recipe.recipe_type
		self.recipes_list[type].add(recipe)
		self.last_update = datetime.datetime.now()

	def print_content_recipe_list(self):
		for key, value in new_book.recipes_list.items():
			print(f"{key} contains : ")
			for i in value:
				print(i.name)


if __name__ == "__main__":
	omelette = Recipe('omelette au fromage', 2, 10, ['eggs', 'cheese', 'pepper'], "", "lunch")
	mozzarella = Recipe('mozzarella_sticks', 3, 20, ['mozzarella', 'sticks'], "", "starter")
	nugget = Recipe('nugget', 4, 65, ['chicken', 'bread'], "", "starter")
	fondant = Recipe('fondant', 4, 30, ['eggs', 'chocolate', 'butter'], "", "dessert")
	recette_to_add = Recipe('pasta', 1, 9, ['pasta', 'water'], "", 'lunch')
	creation = datetime.datetime(2019, 4, 13, 00, 00, 00)
	last = datetime.datetime(2019, 5, 27, 00, 00, 00)
	name = "omelette"
	recipe_list = {
		'starter': {
			mozzarella,
			nugget,
		},
		'lunch': {
			omelette,
		},
		'dessert': {
			fondant,
		}
	}
	new_book = Book("New CookBook", last, creation, recipe_list)
	# print(new_book.get_recipe_by_name('omelette au fromage'))
	# print(new_book.get_recipe_by_name('omelette au fromage'))
	# print(new_book.get_recipes_by_type('starter'))
	# print(f"{new_book.creation_date = }")
	# print(f"{new_book.last_update}")
	# new_book.add_recipe(recette_to_add)
	# print(f"{new_book.last_update}")
	# new_book.print_content_recipe_list()
	# print(creation)
