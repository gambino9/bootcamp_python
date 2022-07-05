import pandas as pd


def how_many_medals_by_country(df, country):
    if not isinstance(df, pd.DataFrame) or not isinstance(country, str):
        return None

    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey',
                   'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
                   'Rugby', 'Lacrosse', 'Polo']
    # Selects rows with corresponding country
    data = df[df.Team == country]
    # Selects rows corresponding to sports list
    data_sport = data[data.Sport.isin(team_sports)]
    # Remove duplicates
    data_sport = data_sport.drop_duplicates(['Year', 'Medal', 'Event'])

    # Selecting rows that don't belong to the sports list
    data_others = data[~data.Sport.isin(team_sports)]
    # Concatenate both dataframes
    concat_data = pd.concat([data_sport, data_others])

    years = concat_data['Year'].unique()
    years = list(map(int, years))
    years = sorted(years)
    total = {}

    for year in years:
        data_year = concat_data[concat_data.Year == year]
        total[year] = {'G': len(data_year[data_year.Medal == 'Gold']),
                       'S': len(data_year[data_year.Medal == 'Silver']),
                       'B': len(data_year[data_year.Medal == 'Bronze']),
                       }
    return total
