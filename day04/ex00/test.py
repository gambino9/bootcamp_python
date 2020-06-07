# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamia <lamia@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/24 23:43:58 by lamia             #+#    #+#              #
#    Updated: 2020/06/07 21:47:03 by lamia            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

df = FileLoader()
ds_path = df.load("../resources/athlete_events.csv")
# open(ds_path
# print(ds_path)