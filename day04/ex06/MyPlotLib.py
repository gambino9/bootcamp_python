# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/29 21:34:06 by lboukrou          #+#    #+#              #
#    Updated: 2020/07/12 21:56:56 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://www.journaldunet.com/solutions/analytics/1210938-le-feature-engineering-futur-du-data-scientist/
# https://towardsdatascience.com/understanding-feature-engineering-part-1-continuous-numeric-data-da4e47099a7b
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.density.html
# https://www.marsja.se/pandas-scatter-matrix-pair-plot/#:~:text=A%20scatter%20matrix%20(pairs%20plot,method%20to%20visualize%20the%20dataset.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html

from FileLoader import FileLoader
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

class MyPLotLib():
	def __init__(self, df, features):
		pass

	def histograms(self, df, features):
		df[features].hist()
		plt.show()

	def density(self, df, features):
		df[features].plot.density()
		plt.show()

	def pair_plot(self, df, features):
		pd.plotting.scatter_matrix(df[features])
		plt.show()

	def box_plot(self, df, features):
		bx = df.boxplot()
		plt.show()