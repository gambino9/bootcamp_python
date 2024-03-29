# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/20 20:52:15 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/24 18:30:21 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# http://www.datasciencemadesimple.com/get-minimum-value-column-python-pandas/

import sys
sys.path.append('../ex00')
from FileLoader import FileLoader
import pandas as pd

def YoungestFellah(df, year):
	"""
	The function returns a dictionary containing the age of the youngest 
	woman and man who took part in the Olympics on that year.
	"""
	data_year = df[df.Year == year]
	data_fem = data_year[data_year.Sex == 'F']
	data_men = data_year[data_year.Sex == 'M']
	min_fem = data_fem['Age'].min()
	min_men = data_men['Age'].min()
	d = {'f' : min_fem, 'm' : min_men}
	return (d)