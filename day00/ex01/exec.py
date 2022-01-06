import sys


def rev_alpha(*args):
    phrase = ""
    for arg in args:
        phrase += " ".join(arg)
    res = phrase.swapcase()
    return res[::-1]


if __name__ == "__main__":
    print(rev_alpha(sys.argv[1:]))
