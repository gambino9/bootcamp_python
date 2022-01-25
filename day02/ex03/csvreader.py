# http://sametmax.com/les-context-managers-et-le-mot-cle-with-en-python/
# https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/3-further/2-context-managers/

import pathlib
import csv


# class CsvReader:
# 	def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
# 		self.filename = filename
# 		self.sep = sep
# 		self.header = header
# 		self.skip_top = skip_top
# 		self.skip_bottom = skip_bottom
#
# 		self.file = None
# 		self.data = []
# 		self.head = None
#
# 	def __enter__(self):
# 		print("Enter")
# 		try:
# 			self.file = open(self.filename)
# 			if self.header is True:
# 				self.head = self.file.readline()
# 			for i in range(0, self.skip_top - 1):
# 				self.file.readline()
# 				print(self.file.readline())
# 			with open(self.filename) as my_file:
# 				lines_count = (sum(1 for _ in my_file))
# 				# print(f"{lines_count=}")
# 			length = 0
# 			for i in range(self.skip_top, lines_count - self.skip_bottom):
# 				line = list(filter(None, self.file.readline().strip().split(self.sep)))
# 				# line = self.file.readline().split(self.sep)
# 				if length == 0:
# 					length = len(line)
# 				assert length == len(line)
# 				# print(line)
# 				self.data.append(line)
# 		except:
# 			print("Error")
# 		# finally:
# 		# 	return self.file
# 		# self.file = open(self.filename)
# 		return self
#
# 	def __exit__(self, type, value, traceback):
# 		print("Close")
# 		self.file.close()
#
# 	def get_data(self):
# 		"""
# 			Retrieves the data/records from skip_top to skip bottom.
# 			Returns:
# 			nested list (list(list, list, ...)) representing the data.
# 		"""
# 		print('plop')
# 		self.file = open(self.filename)
# 		# print(self.file.readline())
# 		print(list(self.file.readline().split(self.sep)))
# 		if self.header is True:
# 			self.head = self.file.readline()
# 		for i in range(0, self.skip_top - 1):
# 			self.file.readline()
# 		with open(self.filename) as my_file:
# 			lines_count = (sum(1 for _ in my_file))
# 			# print(f"{lines_count=}")
# 		length = 0
# 		for i in range(self.skip_top, lines_count - self.skip_bottom):
# 			line = list(filter(None, self.file.readline().strip().split(self.sep)))
# 			# line = self.file.readline().split(self.sep)
# 		return self.data
#
# 	def get_header(self):
# 		"""
# 			Retrieves the header from csv file.
#
# 			@return:
# 			list: representing the data (when self.header is True).
# 			None: (when self.header is False).
# 		"""
# 		print('pouloulou')
# 		return self.head

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
		self.row_len = 0

	def __enter__(self):
		print("Enter")
		self.file_path = pathlib.Path(self.filename)
		self.file = open(self.file_path)
		reader = csv.reader(self.file)

		self.row_len = len(list(reader))
		print(self.row_len)
		print(list(reader))
		if self.header:
			self.head = next(reader)
		for i in range(self.skip_top):
			next(reader)
		# print(list(reader))
		# if self.skip_bottom:
		# print(self.row_len - self.skip_bottom)
		for i in range(self.row_len - self.skip_bottom):
			# print(list(next(reader)))
			self.data.append(list(next(reader)))
		# print(f"blob{next(reader)}")
		# print(self.data)
		return self
		# try:
		# 	self.file = open(self.filename)
		# 	if self.header is True:
		# 		self.head = self.file.readline()
		# 	for i in range(0, self.skip_top - 1):
		# 		self.file.readline()
		# 		print(self.file.readline())
		# 	with open(self.filename) as my_file:
		# 		lines_count = (sum(1 for _ in my_file))
		# 		# print(f"{lines_count=}")
		# 	length = 0
		# 	for i in range(self.skip_top, lines_count - self.skip_bottom):
		# 		line = list(filter(None, self.file.readline().strip().split(self.sep)))
		# 		# line = self.file.readline().split(self.sep)
		# 		if length == 0:
		# 			length = len(line)
		# 		assert length == len(line)
		# 		# print(line)
		# 		self.data.append(line)
		# except:
		# 	print("Error")
		# # finally:
		# # 	return self.file
		# # self.file = open(self.filename)
		# return self

	def __exit__(self, type, value, traceback):
		print("Close")
		self.file.close()

	def get_data(self):
		"""
			Retrieves the data/records from skip_top to skip bottom.
			Returns:
			nested list (list(list, list, ...)) representing the data.
		"""
		# print('plop')
		# self.file = open(self.filename)
		# # print(self.file.readline())
		# print(list(self.file.readline().split(self.sep)))
		# if self.header is True:
		# 	self.head = self.file.readline()
		# for i in range(0, self.skip_top - 1):
		# 	self.file.readline()
		# with open(self.filename) as my_file:
		# 	lines_count = (sum(1 for _ in my_file))
		# 	# print(f"{lines_count=}")
		# length = 0
		# for i in range(self.skip_top, lines_count - self.skip_bottom):
		# 	line = list(filter(None, self.file.readline().strip().split(self.sep)))
		# 	# line = self.file.readline().split(self.sep)
		return self.data


	def get_header(self):
		"""
			Retrieves the header from csv file.

			@return:
			list: representing the data (when self.header is True).
			None: (when self.header is False).
		"""
		print('pouloulou')
		return self.head


if __name__ == "__main__":
	# c = CsvReader('good.csv')
	with CsvReader('good.csv', header=True, skip_top=17) as file:
		data = file.get_data()
		print(data)
		header = file.get_header()
		# print(data)
		# print(header)

# if __name__ == "__main__":
#     with CsvReader('bad.csv') as file:
#         if file == None:
#             print("File is corrupted")
