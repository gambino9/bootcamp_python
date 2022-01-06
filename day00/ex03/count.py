# This script has to be executed in a python console according to the subject

import sys
import string


def text_analyzer(*args):
    if len(args) > 1:
        sys.exit("ERROR")
    if len(args) == 0:
        text = str(input("What is the text to analyze ?\n"))
    else:
        text = args[0]
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punct += 1
        elif char in string.whitespace:
            spaces += 1
    print(f"this text contains: {len(text)} characters :\n"
          f"- {upper} upper letters\n"
          f"- {lower} lower letters\n"
          f"- {punct} punctuations marks\n"
          f"- {spaces} spaces")
