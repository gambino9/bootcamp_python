# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/17 16:26:09 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/18 17:07:51 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#	Interactive guessing number game. Advice : use binary search to solve ;) 
#	Use of random/randint to generate random int
#	Proposed improvements : 
#	- Make small functions for each case

from random import randint

def guess():
	secret = randint(1,99)
	print(secret)
	attempt = 1
	print("This is an interactive guessing game !\nYou have to enter a number betweem 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck !")
	guess = 0
	while ("guess" != secret):
		guess = input("What's your guess between 1 and 99 ?\n")
		try:
			guess = int(guess)
		except ValueError:
			if (guess == "exit"):
				exit()
			else:
				print("That's not a number.")
				continue
		if (guess < secret):
			print("Too low !")
			attempt += 1
		elif (guess > secret):
			print("Too High !")
			attempt += 1
		elif (guess == secret):
			print("Hello")
			print("Congratulations, you've got it !\nYou won in %d attempts" % attempt)
			break
	
guess()