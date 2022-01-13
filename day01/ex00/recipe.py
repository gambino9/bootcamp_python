import sys


class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		# self.name = name
		# self.cooking_lvl = cooking_lvl
		# self.cooking_time = cooking_time
		# self.ingredients = ingredients
		# self.description = description
		# self.recipe_type = recipe_type
		try:
			if not isinstance(name, str) or name == "":
				raise TypeError("ERROR : Name must be a non-empty string")
			self.name = name
			if not isinstance(cooking_lvl, int) or not 0 < cooking_lvl < 6:
				raise TypeError("ERROR : Cooking_level must be a integer between 1 and 5")
			self.cooking_lvl = cooking_lvl
			if not isinstance(cooking_time, int) or cooking_time < 0:
				raise TypeError("ERROR : Cooking time should be a positive integer")
			self.cooking_time = cooking_time
			if not isinstance(ingredients, list) or not all(ingredients) or not all(isinstance(elem, str) for elem in ingredients) or not ingredients:
				raise TypeError("ERROR : Ingredients must be a non-empty list containing strings")
			self.ingredients = ingredients
			if not isinstance(description, str):
				raise TypeError("ERROR : Description must be a string")
			self.description = description
			if recipe_type not in ['starter', 'lunch', 'dessert']:
				raise TypeError("ERROR : Wrong type of recipe")
			self.recipe_type = recipe_type
		except TypeError as te:
			sys.exit(te)

	def __str__(self):
		"""Return the string to print with the recipe info"""
		text = f"The name of this recipe is {self.name}, on a difficulty " \
			   f"cooking scale up to five, it is a {self.cooking_lvl}.\n" \
			   f"It takes {self.cooking_time} minutes to cook.\nIt has the " \
			   f"following ingredients : {self.ingredients}.\nHere is a quick " \
			   f"description : {self.description}.\nThis recipe is a " \
			   f"{self.recipe_type}.\nBon appetit !"
		return text


if __name__ == "__main__":
	nom = "omelette au fromage"
	cook_level = 2
	cook_time = 9
	ingredient = ['eggs', 'cheese', 'pepper']
	# ingredient = []
	descr = 'Une omelette avec du fromage dedans'
	rcp_type = 'lunch'
	rec = Recipe(nom, cook_level, cook_time, ingredient, descr, rcp_type)

	to_print = str(rec)
	print(to_print)
	# print(rec.__str__())
