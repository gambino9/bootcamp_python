# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/24 18:32:11 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/27 19:04:28 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ProportionBySport import ProportionBySport
from FileLoader import FileLoader
import pandas as pd

loader = FileLoader()
df = loader.load('../resources/athlete_events.csv')
year = 2004
sport = 'Tennis'
gender = 'F'
data_year = df[df.Year == year]
data_global_gender = data_year[data_year.Sex == gender]
data_global_gender = data_global_gender.drop_duplicates("Name", keep='first', inplace=False)
data_sport = data_global_gender[data_global_gender.Sport == sport]
d = data_global_gender.shape
df_ndim = data_sport.shape
print("Loading data_sport of dimensions {} x {}".format(df_ndim[0], df_ndim[1]))
print("Loading data_global_gender of dimensions {} x {}".format(d[0], d[1]))
print(data_global_gender)
print("percentage = {}".format((df_ndim[0] * 100) / d[0]))
