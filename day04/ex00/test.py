# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/24 23:43:58 by lamia             #+#    #+#              #
#    Updated: 2020/06/20 20:02:38 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

df = FileLoader()
ds_path = df.load("../resources/athlete_events.csv")
print(type(ds_path))
n = -15
df.display(ds_path, n)
# open(ds_path
# print(ds_path)