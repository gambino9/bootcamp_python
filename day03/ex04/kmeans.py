import numpy as np
from collections import Counter
import pandas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from arg_parse import arguments_parser


class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=4):
		# ... parameters control...
		self.ncentroid = ncentroid  # number of centroids
		self.max_iter = max_iter  # number of max iterations to update the centroids
		self.centroids = []

		path_to_csv = "/home/lamia/bootcamp_python/day03/solar_system_census.csv"
		dataset = pd.read_csv(path_to_csv)

		self.kmeans_model = KMeans(n_clusters=self.ncentroid, max_iter=self.max_iter)

	def fit(self, X):
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns:
		None.
		Raises:
		This function should not raise any Exception.
		"""
		return self.kmeans_model.fit(X)

	def predict(self, X):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns:
		the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		This function should not raise any Exception.
		"""
		return self.kmeans_model.predict(X)

	def plot_kmean(self):
		pass

	def display_coordinates_centroids_and_region(self):
		# Get coordinates of the centroids
		self.centroids = km.kmeans_model.cluster_centers_

		print(f"The centroids are : \n{self.centroids}")

		tallest = max(i[0] for i in self.centroids)
		belt_colony = [i for i in self.centroids if i[0] == tallest]
		slender = min(i[1] for i in self.centroids if (i != belt_colony[0]).all())

		venus_colony = [i for i in self.centroids if i[1] == slender and all(i != belt_colony[0])]
		mars_and_earth_colony = [i for i in self.centroids if (all(i != belt_colony[0]) and all(i != venus_colony[0]))]
		size_mars = max(mars_and_earth_colony[0][0], mars_and_earth_colony[1][0])
		mars_colony = [i for i in self.centroids if i[0] == size_mars]
		earth_colony = [i for i in mars_and_earth_colony if all(i != mars_colony[0])]

		print(f"The belt_colony centroid coordinates are {*belt_colony[0],} because they are the tallest")
		print(f"The venus_colony centroid coordinates are {*venus_colony[0],} because they are the slenderest")
		print(f"The mars_colony centroid coordinates are {*mars_colony[0],} because they are taller than the earth colony")
		print(f"The earth_colony centroid coordinates are {*earth_colony[0],} because they are smaller than the mars colony")

	def print_number_elements_per_centroids(self, prediction):
		self.centroids = km.kmeans_model.cluster_centers_
		label_count = Counter(prediction)

		for i in range(len(label_count)):
			print(f"{label_count[i]} elements in centroid {i}  with coordinates : {self.centroids[i]}")


if __name__ == "__main__":
	path_csv = arguments_parser().filepath
	max_iter = arguments_parser().max_iter
	n_centroids = arguments_parser().n_centroid

	df = pandas.read_csv(path_csv)
	df.drop(columns=df.columns[0], axis=1, inplace=True)

	km = KmeansClustering(max_iter, ncentroid=n_centroids)
	km.fit(df)
	prediction = km.predict(df)

	km.print_number_elements_per_centroids(prediction)
	if n_centroids == 4:
		km.display_coordinates_centroids_and_region()
