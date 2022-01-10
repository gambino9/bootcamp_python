import string
import sys


def filterwords(string, length):
	return [word for word in string if len(word) > length]


if __name__ == "__main__":
	if len(sys.argv) != 3:
		sys.exit("ERROR")

	phrase_list = sys.argv[1].split(" ") if all(elem.isascii() for elem in sys.argv[1].split()) else sys.exit("ERROR")
	lg = int(sys.argv[2]) if sys.argv[2].isdigit() else sys.exit("ERROR")
	p_list = [s.translate(str.maketrans('', '', string.punctuation)) for s in phrase_list]  # removing punctuation
	new_list = filterwords(p_list, lg)
	print(new_list)
