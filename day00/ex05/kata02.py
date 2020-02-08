# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/07 18:42:46 by lboukrou          #+#    #+#              #
#    Updated: 2020/02/08 18:50:44 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
import time

t = (2019, 9, 25, 3, 30)
# t = (2008, 11, 12, 13, 51, 18, 2, 317, 0)
date_str = time.strftime("%Y-%m-%d %H:%M", t)
# time_tuple = (3,30,2019,9,25)
# date_str = time.strftime("%H/%M %Y/%m/%d", time_tupple)
print (date_str)