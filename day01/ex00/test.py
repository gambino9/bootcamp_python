# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/18 17:55:11 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/28 19:29:36 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
from book import Book
from recipe import Recipe

# Example of a recipe
lst = ["chocolat", "oeufs", "farine"]
fondant = Recipe("fondant", 1, 30, lst, "", "dessert")

# Creating object of type 'recipe.Recipe' and printing it
my_str = str(fondant)
print(my_str)

# Examples of other recipes
mozza_sticks = Recipe("mozza sticks", 3, 45, ["mozza", "chapelure", "oeufs"], "", "starter")
veloute = Recipe("veloute", 1, 70, ["légumes", "creme fraiche"], "", "starter")
sandwich = Recipe("sandwich", 1, 10, ["crudites", "jambon"], "", "lunch")
ratatouille = Recipe("ratatouille", 4, 45, ["légumes d'été", "sel et poivre"], "", "lunch")
tarte_citron = Recipe("tarte_au_citron", 3, 60, ["citron", "tarte"], "", "dessert")

cookbook = {
	'starter' :
	{
		mozza_sticks,
		veloute,
	},
	'lunch':{
		# 'sandwich', 
		# 'ratatouille',
	},
	'dessert':{
		# 'fondant',
		# 'tarte au citron',
	}
}

last_up = datetime.datetime.strptime('2020-02-08', "%Y-%m-%d")
crea_date = datetime.datetime.strptime('2020-03-09', "%Y-%m-%d")
livre = Book("livre de recettes", last_up, crea_date, cookbook)
print(livre.last_update)
print(crea_date)
recipes_by_type = livre.get_recipes_by_type("starter")
print(recipes_by_type)

# Example of how to use add_recipe method
# print(cookbook)
mon_cul = []
new_recipe_to_add = livre.add_recipe(ratatouille)
new_recipe_to_add_2 = livre.add_recipe(sandwich)
print(livre.last_update)

# new_recipe_to_add_3 = livre.add_recipe(tarte_citron)
for i in cookbook['lunch']:
	print(i.name)
print(cookbook)
nam_recipe_to_print = livre.get_recipe_by_name(veloute)

# recipe_by_name = livre.get_recipe_by_name("")
# types = get_recipes_by_type(starter)
# print(types)