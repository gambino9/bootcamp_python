# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/29 21:34:17 by lboukrou          #+#    #+#              #
#    Updated: 2020/07/12 21:59:09 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

df = FileLoader()
df = df.load("../resources/athlete_events.csv")
feature1 = 'Height'
feature2 = "Weight"
feat = ['Age', 'Height','Weight', 'Year', 'Team', 'NOC', 'Games']
features = ['Height','Weight']
# print(df.dtypes)

# HISTOGRAM
# df[features].hist()
# plt.show()

# DENSITY (both working)
# df[features].plot.density()
# ax = df[features].plot.kde()
# plt.show()

# PAIR PLOT
# pd.plotting.scatter_matrix(df[features])
# plt.show()

# BOX PLOT
# bx = df.boxplot()
# plt.show()

