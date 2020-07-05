# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/29 21:34:17 by lboukrou          #+#    #+#              #
#    Updated: 2020/07/05 23:06:12 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = FileLoader()
df = df.load("../resources/athlete_events.csv")
features = [f for f in features if np.issubdtype(data[f].dtype, np.number)]
data[features].hist() 
plt.show()