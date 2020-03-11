# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 13:47:22 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/11 14:05:31 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# generateur = (x*x for x in range(6))
# for i in generateur:
# 	print(i)

import random
def generator(text, sep=" ", option=None):
    try:
        assert type(text) == str
        assert option == None or option == 'shuffle' or option == 'unique' or option == 'ordered'
        arr = text.split(sep)
        if option == 'shuffle':
            random.shuffle(arr)
        elif option == 'unique':
            arr = set(arr)
        elif option == 'ordered':
            arr.sort()
        for word in arr:
            yield word
    except:
        print("Error")
# Tests
text = "Le Lorem Ipsum est simplement du faux texte. test test"
print("Generator - Option : None")
for word in generator(text, sep=" "):
    print(word)
print("")
print("Generator - Option : Shuffle")
for word in generator(text, sep=" ", option='shuffle'):
    print(word)
print("")
print("Generator - Option : Unique")
for word in generator(text, sep=" ", option='unique'):
    print(word)
print("")
print("Generator - Option : Ordered")
for word in generator(text, sep=" ", option='ordered'):
    print(word)
print("")