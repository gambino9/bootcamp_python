# http://www.datasciencemadesimple.com/get-minimum-value-column-python-pandas/

import pandas as pd


def youngest_fellah(df, year):
    """
    The function returns a dictionary containing the age of the youngest
    woman and man who took part in the Olympics on that year.
    """
    if not isinstance(df, pd.DataFrame) or not isinstance(year, int):
        return None
    data_year = df[df.Year == year]
    data_fem = data_year[data_year.Sex == 'F']
    data_men = data_year[data_year.Sex == 'M']
    min_fem = data_fem['Age'].min()
    min_men = data_men['Age'].min()
    d = {'f': min_fem, 'm': min_men}
    return d
