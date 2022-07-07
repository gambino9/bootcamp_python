from Komparator import Komparator
from FileLoader import FileLoader

df = FileLoader()
df = df.load("../resources/athlete_events.csv")

komp = Komparator(df)
category = 'Medal'
category1 = 'Sex'
numerical = 'Age'
numerical1 = 'Height'

komp.compare_box_plots(category, numerical)
komp.density(category, numerical)
komp.compare_histograms(category, numerical)
