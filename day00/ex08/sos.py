import sys

morse_alphabet = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	" ": "/",
	"0": "-----",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----."
}


def morse_code(string):
	try:
		upper_string = string.upper()
		morse_string = ""
		for char in upper_string:
			morse_string += morse_alphabet[char]
			morse_string += ' '
		return morse_string[:-1]  # removing last space char
	except KeyError:
		return "ERROR"


if __name__ == "__main__":
	if len(sys.argv) == 1:
		sys.exit()
	s = ' '.join(sys.argv[1:])
	print(morse_code(s))
