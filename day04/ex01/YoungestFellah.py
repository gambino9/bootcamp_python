# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/20 20:52:15 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/21 20:27:58 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd

def YoungestFellah(df, year):
	dic = df.to_dict(orient=dict)
	dic.set_index("Age", drop=True, inplace=True)
	dictionary = df.to_dict(orient=dict)
	# dictionary = dic.to_dict(orient="Age")
	d = {}
	# for k in dic:
		# d[k] =