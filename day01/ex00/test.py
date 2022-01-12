import datetime
from book import Book
from recipe import Recipe
import unittest


class RecipeTest(unittest.TestCase):
	name = "omelette au fromage"
	cook_level = 2
	cook_time = 9
	ingredient = ['eggs', 'cheese', 'pepper']
	descr = 'An omelette with cheese'
	rcp_type = 'lunch'

	def test_recipe_name(self):
		""" Testing if assigning an incorrect name to a recipe raises a system exit"""
		empty_name = ""
		integer_name = 123

		with self.assertRaises(SystemExit):
			recette = Recipe(empty_name, self.cook_level, self.cook_time, self.ingredient, self.descr, self.rcp_type)
		with self.assertRaises(SystemExit):
			recette_2 = Recipe(integer_name, self.cook_level, self.cook_time, self.ingredient, self.descr, self.rcp_type)

	def test_recipe_cook_level(self):
		""" Testing if assigning wrong cook level to a recipe raises a system exit"""
		off_range = 6
		negative_range = -3

		with self.assertRaises(SystemExit):
			recette = Recipe(self.name, off_range, self.cook_time, self.ingredient, self.descr, self.rcp_type)
		with self.assertRaises(SystemExit):
			recette_2 = Recipe(self.name, negative_range, self.cook_time, self.ingredient, self.descr, self.rcp_type)

	def test_recipe_cook_time(self):
		""" Testing if assigning wrong cook time to a recipe raises a system exit"""
		negative_time = -15

		with self.assertRaises(SystemExit):
			recette = Recipe(self.name, self.cook_level, negative_time, self.ingredient, self.descr, self.rcp_type)

	def test_recipe_ingredients(self):
		""" Testing if assigning wrong ingredients to a recipe raises a system exit"""
		empty_ingredients = []
		many_empty_ingredients = ['', '', '']
		different_type_ingredients = ['eggs', 'fromage', 12345]
		non_list_ingredients = "ingredients"

		with self.assertRaises(SystemExit):
			recette = Recipe(self.name, self.cook_level, self.cook_time, empty_ingredients, self.descr, self.rcp_type)
		with self.assertRaises(SystemExit):
			recette = Recipe(self.name, self.cook_level, self.cook_time, many_empty_ingredients, self.descr, self.rcp_type)
		with self.assertRaises(SystemExit):
			recette = Recipe(self.name, self.cook_level, self.cook_time, different_type_ingredients, self.descr, self.rcp_type)
		with self.assertRaises(SystemExit):
			recette = Recipe(self.name, self.cook_level, self.cook_time, non_list_ingredients, self.descr, self.rcp_type)

	def test_recipe_description(self):
		""" Testing if assigning wrong recipe description to a recipe raises a system exit"""
		non_string_description = 12345

		with self.assertRaises(SystemExit):
			recette = Recipe(self.name, self.cook_level, self.cook_time, self.ingredient, non_string_description, self.rcp_type)

	def test_recipe_recipe_type(self):
		""" Testing if assigning wrong recipe type to a recipe raises a system exit"""
		wrong_type = 'apero'

		with self.assertRaises(SystemExit):
			recette = Recipe(self.name, self.cook_level, self.cook_time, self.ingredient, self.descr, wrong_type)

	def test_str_method(self):
		""" Testing if __str__ method returns the expected text"""
		expected_text = f"The name of this recipe is omelette au fromage, on a difficulty " \
			   f"cooking scale up to five, it is a 2.\n" \
			   f"It takes 9 minutes to cook.\nIt has the " \
			   f"following ingredients : ['eggs', 'cheese', 'pepper'].\nHere is a quick " \
			   f"description : An omelette with cheese.\nThis recipe is a " \
			   f"lunch.\nBon appetit !"
		recette = Recipe(self.name, self.cook_level, self.cook_time, self.ingredient, self.descr, self.rcp_type)

		self.assertEqual(str(recette), expected_text)


if __name__ == "__main__":
	unittest.main()
#
# # Creating object of type 'Recipe'
# lst = ["chocolat", "oeufs", "farine"]
# fondant = Recipe("fondant", 1, 30, lst, "", "dessert")
#
# # Using 'str' method to print properly a 'recipe' object into a text
# my_str = str(fondant)
# print(my_str)
#
# # Examples of other recipes
# mozza_sticks = Recipe("mozza sticks", 3, 45, ["mozza", "chapelure", "oeufs"], "", "starter")
# veloute = Recipe("veloute", 1, 70, ["légumes", "creme fraiche"], "", "starter")
# sandwich = Recipe("sandwich", 1, 10, ["crudites", "jambon"], "", "lunch")
# ratatouille = Recipe("ratatouille", 4, 45, ["légumes d'été", "sel et poivre"], "", "lunch")
# tarte_citron = Recipe("tarte_au_citron", 3, 60, ["citron", "tarte"], "", "dessert")
#
# cookbook = {
# 	'starter' :
# 	{
# 		mozza_sticks,
# 		veloute,
# 	},
# 	'lunch':{
# 		# 'sandwich',
# 		# 'ratatouille',
# 	},
# 	'dessert':{
# 		# 'fondant',
# 		# 'tarte au citron',
# 	}
# }
#
# # datetime attributes of a 'book' object
# last_up = datetime.datetime.strptime('2020-02-08', "%Y-%m-%d")
# crea_date = datetime.datetime.strptime('2020-03-09', "%Y-%m-%d")
#
# # Creating object of type 'book'
# livre = Book("livre de recettes", last_up, crea_date, cookbook)
# print(livre.last_update)
# print(crea_date)
#
# # Using 'get_recipes_by_type' method and printing result in form of a list
# recipes_by_type = livre.get_recipes_by_type("starter")
# print(recipes_by_type)
#
# # Example of how to use add_recipe method
# # print(cookbook)
# new_recipe_to_add = livre.add_recipe(ratatouille)
# new_recipe_to_add_2 = livre.add_recipe(sandwich)
# print(livre.last_update)
#
# for i in cookbook['lunch']:
# 	print(i.name)
# print(cookbook)
# # Have to finish 'get_recipe_by_name method'
# nam_recipe_to_print = livre.get_recipe_by_name(veloute)
