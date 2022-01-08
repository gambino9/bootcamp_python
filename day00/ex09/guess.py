import sys
from random import randint


def guess():
	secret = randint(1, 99)
	# print(secret)
	attempt = 0
	print(
		"This is an interactive guessing game !\nYou have to enter a number between 1 and 99 to find out the secret "
		"number.\nType 'exit' to end the game.\nGood luck !")
	while True:
		i = input("What's your guess between 1 and 99 ?\n")
		guess = None
		try:
			guess = int(i)
		except ValueError:
			if i == "exit":
				exit()
			else:
				print("That's not a number.")
				continue
		if guess < secret:
			print("Too low !")
			attempt += 1
		elif guess > secret:
			print("Too High !")
			attempt += 1
		elif guess == secret:
			if guess == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			if attempt == 0:
				print("Congratulations! You got it on your first try!")
			else:
				print(f"Congratulations, you've got it !\nYou won in {attempt + 1} attempts")
			break


if __name__ == "__main__":
	guess()
