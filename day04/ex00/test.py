from FileLoader import FileLoader

df = FileLoader()
ds_path = df.load("../resources/athlete_events.csv")
n = -5
df.display(ds_path, n)
