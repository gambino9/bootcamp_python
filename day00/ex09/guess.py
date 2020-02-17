# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/17 16:26:09 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/17 16:53:30 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint

def guess():
	secret = randint(1,99)
	print(secret)
	attempt = 0
	print("This is an interactive guessing game !\nYou have to enter a number betweem 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck !")

	try:
		guess = int(input("What's your guess between 1 and 99 ?\n"))
	except ValueError:
		print("That's not a number")
	while (guess != secret):
		if (guess < secret):
			print("Too low !")
			guess = int(input("What's your guess between 1 and 99 ?\n"))
			attempt += 1
		elif (guess > secret):
			print("Too High !")
			guess = int(input("What's your guess between 1 and 99 ?\n"))
			attempt += 1
		elif (guess == secret):
			print("Congratulations, you've got it !\n You won in %d attempts", attempt)
			exit()
	
guess()