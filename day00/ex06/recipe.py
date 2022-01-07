import sys

cookbook = {
	'sandwich': {
		'ingredients':
			{
				'ham',
				'bread',
				'cheese',
				'tomatoes'
			},
		'meal': 'lunch',
		'prep_time': '10',
	},
	'cake':
		{
			'ingredients':
				{
					'flour',
					'sugar',
					'eggs'
				},
			'meal': 'dessert',
			'prep_time': '60'
		},
	'salad':
		{
			'ingredients':
				{
					'avocado',
					'arugula',
					'tomatoes',
					'spinach'
				},
			'meal': 'lunch',
			'prep_time': '15'
		}
}


def print_recipe_keys(cookbook_dic):
	for key in cookbook_dic.keys():
		print(key)


def print_recipe_values(cookbook_dic):
	for value in cookbook_dic.values():
		print(value)


def print_recipe_items(cookbook_dic):
	for item in cookbook_dic.items():
		print(item)


def print_recipe(recipe_name):
	print(f"Recipe for {recipe_name}:\n"
		  f"Ingredients list : {', '.join(str(x) for x in cookbook[recipe_name]['ingredients'])}\n"
		  f"To be eaten for {cookbook[recipe_name]['meal']}.\n"
		  f"Takes {cookbook[recipe_name]['prep_time']} minutes of cooking.")


def delete_recipe(recipe_name):
	cookbook.pop(recipe_name)


# name of recipe, ingredients, meal and prep_time
def add_new_recipe(recipe_name, ingredients: list, meal, prep_time):
	new = {
		'ingredients':
			{
				f"{a}" for a in ingredients
			},
		'meal': meal,
		'prep_time': prep_time
	}
	cookbook[recipe_name] = new


def print_all_recipe_names():
	print("The cookbook contains the following recipes :")
	print("\n".join(f"{recipe}" for recipe in cookbook.keys()))


if __name__ == "__main__":
	# existing_name = 'sandwich'
	# new_name = 'omelette au fromage'
	# new_ingredient = ['eggs', 'fromage', 'pepper']
	# new_meal = 'lunch'
	# new_prep_time = 5
	print("Please select an option by typing the corresponding number\n"
		  "1: Add a recipe\n"
		  "2: Delete a recipe\n"
		  "3: Print a recipe\n"
		  "4: Print the cookbook\n"
		  "5: Quit\n")
	while True:
		try:
			choice = int(input())
			if choice == 1:
				try:
					print("To add a new recipe, you must enter the following informations :\n")
					name = str(input("A name : "))
					meal = str(input("A meal type : "))
					time = int(input("The time of preparation : "))
					nbr_ingredients = int(input("The number of ingredients : "))
					print("The ingredients : ")
					# ingredient = list(map(str, input().split()))
					ingredients = [str(input()) for i in range(nbr_ingredients)]
					add_new_recipe(name, ingredients, meal, time)
				except ValueError:
					pass
			elif choice == 2:
				try:
					recipe_to_del = str(input("Please enter the name of the recipe to delete :\n"))
					delete_recipe(recipe_to_del)
				except ValueError:
					pass
				except NameError:
					print("This recipe is not in the cookbook.\n")
			elif choice == 3:
				try:
					recipe_to_print = str(input("Please enter the recipe's name to get its details :\n"))
					print_recipe(recipe_to_print)
				except ValueError:
					pass
				except NameError:
					pass
			elif choice == 4:
				print_all_recipe_names()
			elif choice == 5:
				print("Cookbook closed.\nGood-bye !")
				sys.exit()
		except ValueError:
			print("This option does not exist, please type the corresponding "
				  "number.\nTo exit, enter 5.\n")
			continue
