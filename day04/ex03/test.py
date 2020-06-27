# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/27 20:36:59 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/27 21:00:16 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from HowManyMedals import HowManyMedals
from FileLoader import FileLoader
import pandas as pd

loader = FileLoader()
df = loader.load('../resources/athlete_events.csv')
name = 'Kjetil Andr Aamodt'
data_years = df[df.Name == name]
data_years = data_years.dropna()
dic = {}
print(data_years)