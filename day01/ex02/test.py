from vector import Vector, VectorError
import unittest


class VectorConstructorTest(unittest.TestCase):
	def test_vector_with_simple_list(self):
		"""
		Testing instance of Vector with simple list
		Is shape correct
		Is assigning Vector with list of int raises a VectorError
		"""
		f_list = ([0.0, 1.0, 2.0, 3.0])
		i_list = ([0, 1, 2, 3])
		expected_shape = (1, 4)
		v = Vector(f_list)

		self.assertTrue(v.shape == expected_shape)
		with self.assertRaises(VectorError):
			v1 = Vector(i_list)

	def test_vector_with_list_of_lists(self):
		"""
		Testing instance of Vector with list of lists
		Is shape correct
		Is assigning Vector with list of lists of int raises a VectorError
		"""
		f_list = ([[0.0], [1.0], [2.0], [3.0]])
		i_list = ([[0], [1], [2], [3]])
		expected_shape = (4, 1)
		v = Vector(f_list)

		self.assertTrue(v.shape == expected_shape)
		with self.assertRaises(VectorError):
			v1 = Vector(i_list)

	def test_vector_with_integer(self):
		"""
			Testing instance of Vector with integer as a size
			Is shape correct
			Is values created is correct
		"""
		integer_size = 3
		v = Vector(integer_size)
		expected_shape = (3, 1)
		expected_values = [[0.0], [1.0], [2.0]]

		self.assertTrue(v.shape == expected_shape)
		self.assertTrue(v.values == expected_values)

	def test_vector_with_range(self):
		"""
			Testing instance of Vector with range
			Is shape correct
			Is values created is correct
		"""
		vec_range = range(10, 15)
		v = Vector(vec_range)
		expected_shape = (5, 1)
		expected_values = [[10.0], [11.0], [12.0], [13.0], [14.0]]

		self.assertTrue(v.shape == expected_shape)
		self.assertTrue(v.values == expected_values)

	def test_vector_with_tuple(self):
		"""
			Testing instance of Vector with tuple as a range
			Is shape correct
			Is values created is correct
		"""
		vec_tuple = (10, 15)
		v = Vector(vec_tuple)
		expected_shape = (5, 1)
		expected_values = [[10.0], [11.0], [12.0], [13.0], [14.0]]

		self.assertTrue(v.shape == expected_shape)
		self.assertTrue(v.values == expected_values)


class VectorDunderMethodsTest(unittest.TestCase):
	def test_vector_add(self):
		v1 = Vector([[1.0], [2.0], [3.0]])
		v2 = Vector([[2.0], [4.0], [8.0]])
		v3 = Vector([1.0, 2.0, 3.0])
		v4 = Vector([2.0, 4.0, 8.0])

		expected1 = Vector([[3.0], [6.0], [11.0]])
		expected2 = Vector([3.0, 6.0, 11.0])

		v5 = v1 + v2
		v6 = v3 + v4
		self.assertTrue(isinstance(v5, Vector))
		self.assertTrue(isinstance(v6, Vector))
		self.assertTrue(v5.shape == expected1.shape)
		self.assertTrue(v5.values == expected1.values)
		self.assertTrue(v6.shape == expected2.shape)
		self.assertTrue(v6.values == expected2.values)

	def test_vector_sub(self):
		v1 = Vector([[2.0], [4.0], [8.0]])
		v2 = Vector([[1.0], [2.0], [3.0]])
		v3 = Vector([2.0, 4.0, 8.0])
		v4 = Vector([1.0, 2.0, 3.0])

		expected1 = Vector([[1.0], [2.0], [5.0]])
		expected2 = Vector([1.0, 2.0, 5.0])

		v5 = v1 - v2
		v6 = v3 - v4
		self.assertTrue(isinstance(v5, Vector))
		self.assertTrue(isinstance(v6, Vector))
		self.assertTrue(v5.shape == expected1.shape)
		self.assertTrue(v5.values == expected1.values)
		self.assertTrue(v6.shape == expected2.shape)
		self.assertTrue(v6.values == expected2.values)


if __name__ == "__main__":
	unittest.main()
