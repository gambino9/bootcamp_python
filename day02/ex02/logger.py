# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 20:36:17 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/11 21:34:21 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# http://gillesfabio.com/blog/2010/12/16/python-et-les-decorateurs/
# https://www.askpython.com/python/environment-variables-in-python

import os
import time
import datetime
from random import randint

def log(funct):
	start = datetime.datetime.now()
	print("Hello")
	end = datetime.datetime.now()
	res = end - start
	print(res)
	# print("(%s)Running: %s" % (os.environ['USER'], funct.__name__))
	return (funct)

class CoffeeMachine():
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