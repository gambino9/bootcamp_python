# https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/

import pandas as pd


def ProportionBySport(df, olympic_year, olympic_sport, specific_gender):
	"""
	The function returns a float corresponding to the proportion (percentage)
	of participants who played the given sport among the participants of the
	given gender.
	The function answers questions like the following : “What was the
	percentage of female basketball players among all the female participants
	of the 2016 Olympics?”
	"""
	if not isinstance(df, pd.DataFrame):
		return None
	if not isinstance(olympic_year, int):
		return None
	if not isinstance(olympic_sport, str) or not (isinstance(specific_gender, str)):
		return None
	year = olympic_year
	sport = olympic_sport
	gender = specific_gender
	# number of athletes during one year
	data_year = df[df.Year == year]
	# number of athletes of specific gender in that specific year
	data_year_gender = data_year[data_year.Sex == gender]
	# drop duplicate of ID instead of name because it is more accurate
	data_year_gender = data_year_gender.drop_duplicates(['ID'])
	# number of a specific sport's athletes of specific gender
	data_year_gender_sport = data_year_gender[data_year_gender.Sport == sport]
	# dimensions of the dataframes
	d = len(data_year_gender_sport.index)
	res = d / len(data_year_gender.index)
	res = ('%.3f' % res)
	return res
