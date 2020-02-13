# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 17:34:28 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/13 19:31:20 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#	Getting to know about nested dictionnaries

cookbook = {
	'sandwich': {
		'ingredients':
		{
			'ham',
			'bread',
			'cheese',
			'tomatoes'
		},
		'meal': 	'lunch',
		'prep_time': '10',
	},
	'cake' :
	{
		'ingredients':
		{
			'flour',
			'suggar',
			'eggs'
		},
		'meal': 'dessert',
		'prep_time': '60'
	},
	'salad' :
	{
		'ingredients':
		{
			'avodado',
			'arugula',
			'tomatoes',
			'spinach'
		},
		'meal': 'lunch',
		'prep_time': '15'
	}
}

#	1- How to only print the keys
for i in cookbook.keys():
	print(i)

#	2- How to only print the values
# for i in cookbook.values():
# 	print(i)

#	3- How to only print the items
# for i in cookbook.items():
# 	print(i)

#	Print what's inside the meals

# for k, v in cookbook.items():
#     for k1, v1 in v.items():
#         print(k1)

#	Function to print a recipe from cookbook. Param : name recipe

# def print_recipe(cookbook.value()):
# 	for i in cookbook.values():
# 		print(i)



