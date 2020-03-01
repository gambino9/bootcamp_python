# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/18 17:55:11 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/29 18:25:08 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
from book import Book
from recipe import Recipe

# Creating object of type 'Recipe'
lst = ["chocolat", "oeufs", "farine"]
fondant = Recipe("fondant", 1, 30, lst, "", "dessert")

# Using 'str' method to print properly a 'recipe' object into a text
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

# datetime attributes of a 'book' object
last_up = datetime.datetime.strptime('2020-02-08', "%Y-%m-%d")
crea_date = datetime.datetime.strptime('2020-03-09', "%Y-%m-%d")

# Creating object of type 'book'
livre = Book("livre de recettes", last_up, crea_date, cookbook)
print(livre.last_update)
print(crea_date)

# Using 'get_recipes_by_type' method and printing result in form of a list
recipes_by_type = livre.get_recipes_by_type("starter")
print(recipes_by_type)

# Example of how to use add_recipe method
# print(cookbook)
new_recipe_to_add = livre.add_recipe(ratatouille)
new_recipe_to_add_2 = livre.add_recipe(sandwich)
print(livre.last_update)

for i in cookbook['lunch']:
	print(i.name)
print(cookbook)
# Have to finish 'get_recipe_by_name method'
nam_recipe_to_print = livre.get_recipe_by_name(veloute)
