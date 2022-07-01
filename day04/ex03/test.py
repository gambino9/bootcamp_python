from HowManyMedals import how_many_medals
from FileLoader import FileLoader

loader = FileLoader()
df = loader.load('../resources/athlete_events.csv')
name = 'Kjetil Andr Aamodt'
name_1 = 'Gary Abraham'
name_2 = 'Yekaterina Konstantinovna Abramova'
name_3 = 'Kristin Otto'
medals = how_many_medals(df, name)
medals_1 = how_many_medals(df, name_1)
medals_2 = how_many_medals(df, name_2)
medals_3 = how_many_medals(df, name_3)

print(medals)
print(name)
for i in medals:
    print(i, medals[i])

print(name_1)
for i in medals_1:
    print(i, medals_1[i])

print(name_2)
for i in medals_2:
    print(i, medals_2[i])

print(name_3)
for i in medals_3:
    print(i, medals_3[i])
