import sys


def filterwords(string, length):
	return [word for word in string if len(word) > lg]


if __name__ == "__main__":
	phrase = sys.argv[1].split(" ") if all(elem.isalnum() for elem in sys.argv[1].split()) else sys.exit("ERROR")
	lg = int(sys.argv[2]) if sys.argv[2].isdigit() else sys.exit("ERROR")
	new_list = filterwords(phrase, lg)
	print(new_list)
