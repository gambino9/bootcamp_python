# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/28 19:35:25 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/29 20:52:17 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/
# https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column

from FileLoader import FileLoader
import pandas as pd

"""
Write a class calledSpatioTemporalDatawhich takes a dataset (pandas DataFrame)
as argument in itsconstructor and implements the following methods:
"""
class SpatioTemporalData:
	def __init__(self, df):
		self.df = df
		pass

	"""
	when(location): This method takes a location as an argument and returns
	a list containing the years where games were held in the given location.
	"""
	def when(self, location):
		data_when = self.df[self.df.City == location]
		# unique() prints 'year' values in order of appearance without duplicates
		# it returns a panda array, so we cast it into a list
		years = data_when['Year'].unique()
		years = list(years)
		return (years)
		pass

	"""
	where(date): This method takes a date as an argument and returns the
	location where the Olympics took place in the given year.
	"""
	def where(self, date):
		data_where = self.df[self.df.Year == date]
		return (data_where.City.iloc[0])
		pass
