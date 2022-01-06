import sys


def whois(number):
	if not number.isdigit():
		return "ERROR"
	else:
		num = int(number)
		if num == 0:
			return "I'm Zero."
		return "I'm Even." if num % 2 == 0 else "I'm Odd."


if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit("ERROR")
	print(whois(sys.argv[1]))
