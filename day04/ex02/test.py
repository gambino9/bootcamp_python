from ProportionBySport import ProportionBySport
from FileLoader import FileLoader

loader = FileLoader()
df = loader.load('../resources/athlete_events.csv')

year = 2004
sport = 'Tennis'
gender = 'F'
proportion = ProportionBySport(df, year, sport, gender)
print(proportion)

year_1 = 2008
sport_1 = 'Hockey'
gender_1 = 'F'
proportion_1 = ProportionBySport(df, year_1, sport_1, gender_1)
print(proportion_1)

year_2 = 1964
sport_2 = 'Biathlon'
gender_2 = 'M'
proportion_2 = ProportionBySport(df, year_2, sport_2, gender_2)
print(proportion_2)

