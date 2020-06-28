# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/28 19:35:25 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/28 20:43:51 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/

from FileLoader import FileLoader
import pandas as pd

"""
Write a class calledSpatioTemporalDatawhich takes a dataset (pandas DataFrame)
as argument in itsconstructor and implements the following methods:
"""
class SpatioTemporalData:
	def __init__(self, df):
		pass

	"""
	when(location): This method takes a location as an argument and returns
	a list containing the years where games were held in the given location.
	"""
	def when(self, location):
		pass

	"""
	where(date): This method takes a date as an argument and returns the
	location where the Olympics took place in the given year.
	"""
	def where(self, date):
		data_where = self.df[self.df.Year == year]
		return (data_where.City.iloc[0])
		pass
