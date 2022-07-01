# https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
# https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas

import pandas as pd


def how_many_medals(df, name):
    """
    The function returns a dictionary of dictionaries giving the number and
    type of medals for each year during which the participant won medals.
    """
    if not isinstance(df, pd.DataFrame) or not isinstance(name, str):
        return None

    # Keep the rows containing only the name
    data_years = df[df.Name == name]
    # data_years = data_years.dropna()
    years = data_years['Year'].unique()
    total = {}
    for year in years:
        # Keeping the rows containing only the year for each year iterated
        dy = data_years[data_years.Year == int(year)]
        total[year] = {'G': len(dy[dy.Medal == 'Gold']),
                       'S': len(dy[dy.Medal == 'Silver']),
                       'B': len(dy[dy.Medal == 'Bronze'])}
    return total
