# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/21 18:30:07 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/24 18:31:55 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
from YoungestFellah import YoungestFellah
import pandas as pd

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
year = 2004
data_year = data[data.Year == year]
fem = data_year[data_year.Sex == 'F']
men = data_year[data_year.Sex == 'M']
print(fem['Age'].min())
print(men['Age'].min())
d = {'f' : fem['Age'].min(), 'm' : men['Age'].min()}
print(type(d))