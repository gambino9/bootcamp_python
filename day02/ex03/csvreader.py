# http://sametmax.com/les-context-managers-et-le-mot-cle-with-en-python/
# https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/3-further/2-context-managers/
import pathlib
import csv
import sys


class CsvReader:
	def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

		self.file = None
		self.data = []
		self.head = None
		self.file_path = None

	def __enter__(self):
		self.file_path = pathlib.Path(self.filename)

		try:
			self.file = open(self.file_path)
		except FileNotFoundError as e:
			sys.exit(e)

		reader = csv.reader(self.file)

		if self.header:
			self.head = next(reader)
		self.data = [i for i in reader]

		# Check if all rows are the same size as the header
		# At each iteration, the row is converted to a string to check its length
		# We also check for empty elements in list
		for sub_list in self.data:
			if '' in sub_list:
				return None
			if not len(','.join(sub_list).split(self.sep)) == len(self.data[0]):
				return None
		return self

	def __exit__(self, type, value, traceback):
		self.file.close()

	def getdata(self):
		"""
			Retrieves the data/records from skip_top to skip bottom.
			Returns:
			nested list (list(list, list, ...)) representing the data.
		"""
		self.data = self.data[self.skip_top:-self.skip_bottom if self.skip_bottom != 0 else None]
		return self.data

	def getheader(self):
		"""
			Retrieves the header from csv file.

			@return:
			list: representing the data (when self.header is True).
			None: (when self.header is False).
		"""
		if self.header is False:
			return None
		return self.head

	def __str__(self):
		return '\n'.join(str(i) for i in self.data)


if __name__ == "__main__":
	with CsvReader('god.csv', skip_top=18, skip_bottom=0) as file:
		if file is None:
			print("File is corrupted or missing")
		else:
			print(file.getheader(), end="\n")
			print(file.getdata(), end="\n\n")

	with CsvReader('good.csv', header=True, skip_top=17, skip_bottom=0) as file:
		if file is None:
			print("File is corrupted or missing")
		else:
			print(file.getheader(), end="\n")
			print(file.getdata(), end="\n\n")

	with CsvReader('bad.csv') as file:
		if file is None:
			print("File is corrupted")
