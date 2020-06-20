# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/24 17:37:39 by lamia             #+#    #+#              #
#    Updated: 2020/06/20 20:02:57 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://www.geeksforgeeks.org/python-pandas-df-size-df-shape-and-df-ndim/

import pandas as pd

class FileLoader():
    def __init__(self):
        pass
    
    def load(self, path):
        """
        The argument of this method is the file path of the dataset to
        load. It must display a message specifying the dimensions of the
        dataset (e.g. 340 x 500). The method returns the dataset loaded
        as a pandas.DataFrame.
        """
        data = pd.read_csv(path)
        # Here we get the dimensions of the csv under form of a tuple
        df_ndim = data.shape
        print("Loading dataset of dimensions {} x {}".format(df_ndim[0], df_ndim[1]))
        return (data)
        pass

    def display(self, df, n):
        df = df
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(n * -1))
        pass