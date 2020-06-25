# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/24 18:32:11 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/25 20:35:46 by lboukrou         ###   ########.fr        #
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
# Sportifs durant une annee
data_year = df[df.Year == year]
# tennismen durant cette annee
data_global_gender = data_year[data_year.Sex == gender]
# genre specifique de tennismen durant cette annee
# data_gender = data_sport[data_sport.Sex == gender]
# genre specifique global durant cette annee
# print(type(data_gender))
# df_nd = data_gender.shape
data_global_gender = data_global_gender.drop_duplicates("Name", keep='first', inplace=False)
data_sport = data_global_gender[data_global_gender.Sport == sport]
d = data_global_gender.shape
df_ndim = data_sport.shape
print("Loading data_sport of dimensions {} x {}".format(df_ndim[0], df_ndim[1]))
# print("Loading data_gender of dimensions {} x {}".format(df_nd[0], df_nd[1]))
print("Loading data_global_gender of dimensions {} x {}".format(d[0], d[1]))
print(data_global_gender)

# df_filter = df[df.Sex == gender]
# gender_count = df_filter.shape[0]
# df_filter_sport = df_filter[df_filter.Sport == sport]
# print(df_filter_sport.shape[0] / gender_count)
# print(df_filter_sport.shape[0])
# print(gender_count)
