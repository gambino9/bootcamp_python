tup = (19, 42, 21)


def kata00(numbers):
	print(f"The {len(numbers)} numbers are : {', '.join(str(a) for a in numbers)}")
	print("the 3 numbers are : %d, %d, %d" % (tup[0], tup[1], tup[2]))


if __name__ == "__main__":
	kata00(tup)
