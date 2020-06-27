# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ProportionBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/24 18:23:15 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/27 19:06:37 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/

from FileLoader import FileLoader
import pandas as pd


def ProportionBySport(df, olympic_year, olympic_sport, specific_gender):
	"""
	The function returns a float corresponding to the proportion (percentage)
	of participants who played the givensport among the participants of the
	given gender.
	The function answers questions like the following : “What was the
	percentage of female basketball players amongall the female participants
	of the 2016 Olympics?”
	"""
	year = olympic_year
	sport = olympic_sport
	gender = specific_gender
	# number of athletes during one year
	data_year = df[df.Year == year]
	# number of atheletes of specific gender in that specific year
	data_global_gender = data_year[data_year.Sex == gender]
	# removing duplicate athletes
	data_global_gender = data_global_gender.drop_duplicates("Name", keep='first', inplace=False)
	# number of a specific sport's athletes of specific gender 
	data_sport = data_global_gender[data_global_gender.Sport == sport]
	# dimensions of the dataframes
	d = data_global_gender.shape
	df_ndim = data_sport.shape
	return((df_ndim[0] * 100) / d[0])