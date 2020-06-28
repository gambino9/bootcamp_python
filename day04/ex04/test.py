# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/28 19:35:38 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/28 20:40:05 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd

df = FileLoader()
df = df.load("../resources/athlete_events.csv")
year = 2016
location = 'Paris'
data_when = df[df.Year == year]
data_where = df[df.City == location]
print(data_when)


data_when = data_when.City.iloc[0]
print(data_when)
print(type(data_when))