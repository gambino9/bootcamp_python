# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamia <lamia@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/29 21:34:17 by lboukrou          #+#    #+#              #
#    Updated: 2020/07/12 00:51:38 by lamia            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = FileLoader()
df = df.load("../resources/athlete_events.csv")
feature1 = 'Height'
feature2 = "Weight"
features = ['Height','Weight']
# print(df.dtypes)

# HISTOGRAM
# print(type(features))
# df[features].hist()
# plt.show()

# DENSITY (test school)
# df[feature1].plot.density()

# PAIR PLOT

