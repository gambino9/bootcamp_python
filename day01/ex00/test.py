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
			recette_2 = Recipe(self.name, self.cook_level, self.cook_time, many_empty_ingredients, self.descr, self.rcp_type)
		with self.assertRaises(SystemExit):
			recette_3 = Recipe(self.name, self.cook_level, self.cook_time, different_type_ingredients, self.descr, self.rcp_type)
		with self.assertRaises(SystemExit):
			recette_4 = Recipe(self.name, self.cook_level, self.cook_time, non_list_ingredients, self.descr, self.rcp_type)

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


class BookTest(unittest.TestCase):
	mozzarella = Recipe('mozzarella_sticks', 3, 20, ['mozzarella', 'sticks'], "", "starter")
	nugget = Recipe('nugget', 4, 65, ['chicken', 'bread'], "", "starter")
	omelette = Recipe('omelette au fromage', 2, 10, ['eggs', 'cheese', 'pepper'], "", "lunch")
	fondant = Recipe('fondant', 4, 30, ['eggs', 'chocolate', 'butter'], "", "dessert")
	creation = datetime.datetime(2019, 4, 13, 00, 00, 00)
	last = datetime.datetime(2019, 5, 27, 00, 00, 00)
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
	test_book = Book("Text Book", last, creation, recipe_list)

	def test_get_recipe_by_type_method(self):
		gibberish_type = "blabla"
		integer_type = 123

		with self.assertRaises(SystemExit):
			self.test_book.get_recipes_by_type(gibberish_type)
			self.test_book.get_recipes_by_type(integer_type)

	def test_get_recipe_by_name_method(self):
		non_existing_name = "blabla"
		int_name = 123
		empty_name = ""

		with self.assertRaises(SystemExit):
			self.test_book.get_recipes_by_type(non_existing_name)
			self.test_book.get_recipes_by_type(int_name)
			self.test_book.get_recipes_by_type(empty_name)

	def test_add_recipe_method(self):
		non_recipe_object = "blabla"

		with self.assertRaises(SystemExit):
			self.test_book.add_recipe(non_recipe_object)

	def test_add_recipe_does_the_adding(self):
		recipe_to_add = Recipe('pasta', 1, 9, ['pasta', 'water'], "", 'lunch')
		self.test_book.add_recipe(recipe_to_add)
		type_of_added_recipe = recipe_to_add.recipe_type

		self.assertIn(recipe_to_add, self.test_book.recipes_list[type_of_added_recipe])

	def test_add_recipe_method_update_time(self):
		recipe_to_add = Recipe('cheesecake', 5, 45, ['cheese', 'cake'], "", 'dessert')
		last_update1 = self.test_book.last_update
		self.test_book.add_recipe(recipe_to_add)
		self.test_book.print_content_recipe_list()
		last_update2 = self.test_book.last_update

		self.assertNotEqual(last_update1, last_update2)


if __name__ == "__main__":
	unittest.main()
