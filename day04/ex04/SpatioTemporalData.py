# https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/
# https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column


class SpatioTemporalData:
	def __init__(self, df):
		self.df = df

	"""
	Takes a location as an argument and returns a list containing 
	the years where games were held in the given location.
	"""
	def when(self, location):
		if not isinstance(location, str):
			return None
		data_when = self.df[self.df.City == location]
		# unique() prints 'year' values in order of appearance without duplicates
		# it returns a panda array, so we cast it into a list
		years = data_when['Year'].unique()
		years = list(years)
		return years

	"""
	Takes a date as an argument and returns the location 
	where the Olympics took place in the given year.
	"""
	def where(self, date):
		if not isinstance(date, int):
			return None
		data_where = self.df[self.df.Year == date]
		cities = data_where['City'].unique()
		cities = list(cities)
		return cities
