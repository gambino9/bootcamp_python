# https://www.journaldunet.com/solutions/analytics/1210938-le-feature-engineering-futur-du-data-scientist/
# https://towardsdatascience.com/understanding-feature-engineering-part-1-continuous-numeric-data-da4e47099a7b
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.density.html
# https://www.marsja.se/pandas-scatter-matrix-pair-plot/#:~:text=A%20scatter%20matrix%20(pairs%20plot,method%20to%20visualize%20the%20dataset.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


class MyPLotLib:
    def __init__(self):
        pass

    def histograms(self, df, features):
        if not isinstance(df, pd.DataFrame) or not isinstance(features, list) \
                or len(features) == 0:
            return None
        df[features].hist()
        plt.show()

    def density(self, df, features):
        if not isinstance(df, pd.DataFrame) or not isinstance(features, list) \
                or len(features) == 0:
            return None
        df[features].plot.density()
        # This method works too
        # ax = df[features].plot.kde()
        plt.show()

    def pair_plot(self, df, features):
        if not isinstance(df, pd.DataFrame) or not isinstance(features, list) \
                or len(features) == 0:
            return None
        pd.plotting.scatter_matrix(df[features])
        plt.show()

    def box_plot(self, df, features):
        if not isinstance(df, pd.DataFrame) or not isinstance(features, list) \
                or len(features) == 0:
            return None
        fig, axs = plt.subplots()
        a = pd.array(df[features])
        axs.boxplot(df[features].dropna(), labels=features)
        matplotlib.pyplot.show()
