from FileLoader import FileLoader
from MyPlotLib import MyPLotLib

df = FileLoader()
df = df.load("../resources/athlete_events.csv")
feature1 = ['Height']
feature2 = ['Weight']
feat = ['Age', 'Height', 'Weight', 'Year']
features = ['Height', 'Weight']

mplt = MyPLotLib()

mplt.histograms(df, features)
mplt.density(df, features)
mplt.pair_plot(df, features)
mplt.box_plot(df, features)
