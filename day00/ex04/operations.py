import sys


def operations(a, b):
    print("Sum		:", a + b)
    print("Difference	:", a - b)
    print("Product		:", a * b)
    try:
        print("Quotient	:", a / b)
        print("Remainder	:", a % b)
    except ZeroDivisionError:
        print("Quotient 	: ERROR (div by zero)")
        print("Remainder 	: ERROR (div by zero)")


if __name__ == "__main__":
    usage = "Usage : python operation.py <number1> <number2>\nExample :\n\tpython operations.py 10 3"
    if len(sys.argv) == 3:
        try:
            operations(int(sys.argv[1]), int(sys.argv[2]))
        except ValueError:
            sys.exit(f"InputError : Only numbers\n\n{usage}")
    else:
        if len(sys.argv) > 3:
            print("InputError : Too many arguments\n")
        print(usage)
