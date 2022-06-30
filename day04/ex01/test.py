from FileLoader import FileLoader
from YoungestFellah import youngest_fellah

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
year = 1992
year_1 = 2004
year_2 = 2010
year_3 = 2003

res = youngest_fellah(data, year)
res_1 = youngest_fellah(data, year_1)
res_2 = youngest_fellah(data, year_2)
res_3 = youngest_fellah(data, year_3)
print(f"Youngest woman and man in the year {year} are {res}")
print(f"Youngest woman and man in the year {year_1} are {res_1}")
print(f"Youngest woman and man in the year {year_2} are {res_2}")
print(f"Youngest woman and man in the year {year_3} are {res_3}")
