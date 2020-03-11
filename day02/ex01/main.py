# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 18:25:34 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/11 19:45:26 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# getattr(object, name[, default])
# Return the value of the named attribute of object. name must be a string.
# If the string is the name of one of the object’s attributes, the result is
# the value of that attribute.

# setattr(object, name, value)
# This is the counterpart of getattr(). The arguments are an object, a string
# and an arbitrary value. The string may name an existing attribute or a new
# attribute. The function assigns the value to the attribute, provided
# the object allows it.

def what_are_the_vars(*args, **kwargs):
	obj = ObjectC()
	ind = 0
	for i in args:
		setattr(obj, "var_"+ str(ind), i)
		ind += 1
	for k, v in kwargs.items():
		try:
			getattr(obj, k)
		except:
			setattr(obj, k, v)
		else:
			return (None)
	return (obj)

class ObjectC(object):
	def __init__(self):
		pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value= getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__== "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj= what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj= what_are_the_vars()
	doom_printer(obj)
	obj= what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj= what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
