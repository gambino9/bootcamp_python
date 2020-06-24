# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ProportionBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/24 18:23:15 by lboukrou          #+#    #+#              #
#    Updated: 2020/06/24 18:31:57 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd

def ProportionBySport(df, year, sport, gender):
	"""
	The function returns a float corresponding to the proportion (percentage)
	of participants who played the givensport among the participants of the
	given gender.
	The function answers questions like the following : “What was the
	percentage of female basketball players amongall the female participants
	of the 2016 Olympics?”
	"""
	