# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/13 19:31:24 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/13 20:11:44 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#	Discovering list comprehensions

a = [1,4,2,7,1,9,0,3,4,6,6,6,8,3]
c = "Bonjour les amis, ca va ou quoi ?"
b = []
d = []
n = 4

for word in c.split():
	if len(word) < n:
		continue
	else:
		d

# print(b)
print(d)