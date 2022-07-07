# https://www.w3schools.com/python/matplotlib_subplot.asp


import matplotlib.pyplot as plt
import pandas as pd


class Komparator:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            return
        self.df = df.dropna()

    def compare_box_plots(self, categorical_var, numerical_var):
        """
        Displays a series of box plots to compare how the distribution of
        the numerical variable changes if we only consider the subpopulation
        which belongs to each category. There should be as many box plots as
        categories. For example, with Sex and Height, we would compare the
        height distributions of men vs. women with two box plots.
        """
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            return None
        # One boxplot will be made per categorical_var because of 'by'
        self.df.boxplot(column=[numerical_var], by=categorical_var)
        plt.show()

    def density(self, categorical_var, numerical_var):
        """
        displays the density of the numerical variable. Each subpopulation
        should be represented by a separate curve on the graph.
        """
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            return None
        column_cat = list(self.df[categorical_var].unique())
        for cat in column_cat:
            # variable is named 'mask' to indicate a boolean array
            mask = self.df[categorical_var] == cat
            data = self.df[mask][numerical_var]
            data.plot(kind='density', label=cat, legend=True)
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        """
        lots the numerical variable in a separate histogram for each category
        As an extra, you can use overlapping histograms with a color code.
        """
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            return None

        column_cat = list(self.df[categorical_var].unique())
        # create the plot
        fig, ax = plt.subplots(ncols=len(column_cat))

        for index, cat in enumerate(column_cat):
            m = self.df[categorical_var] == cat
            # set title to the graph
            ax[index].set_title(cat)
            # Creates the histogram for each categorical value
            ax[index].hist(self.df[m][numerical_var].dropna())
            # add a grid to the graph
            ax[index].grid()
        plt.show()

