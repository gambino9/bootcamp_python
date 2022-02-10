import os
import time
from random import randint


def log(func):
	def print_log(*args, **kwargs):
		start = time.time()
		ret = func(*args, **kwargs)
		end = time.time()
		exec_time = end - start
		with open('machine.log', 'a') as file:
			content = f"({os.environ['USER']})Running : {str(func.__name__).capitalize():19}" \
						f"[ exec-time = {exec_time:.4f} {'s' if exec_time > 1 else 'ms'}]\n"
			file.write(content)
			file.close()
		return ret

	return print_log


class CoffeeMachine:
	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")


if __name__ == "__main__":

	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()

	machine.make_coffee()
	machine.add_water(70)
