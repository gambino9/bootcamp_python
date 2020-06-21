# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/21 18:30:07 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/21 20:56:51 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
from YoungestFellah import YoungestFellah
import pandas as pd

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
year = 2002
# data_year = (data.Year==year) == True
data_year = data[data.Year == year]
print(data_year)
data.to_dict('dict')
print(type(data))
# print(data.Age.min)
print(type(data.Sex))