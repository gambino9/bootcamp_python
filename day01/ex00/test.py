# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/18 17:55:11 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/24 21:45:25 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# from book import Book
from recipe import Recipe

lst = ["chocolat", "oeufs", "farine"]
fondant = Recipe("fondant", 1, 30, lst, "", "dessert")
my_str = str(fondant)
print(my_str)