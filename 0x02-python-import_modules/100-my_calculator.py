#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def main():
    argc = len(sys.argv)
    if argc != 4:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        sys.exit(1)

    operators = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
            }

    if sys.argv[2] in operators:
        number1 = int(sys.argv[1])
        number2 = int(sys.argv[3])
        operator = operators[sys.argv[2]]
        result = operator(number1, number2)
        print(f"{number1} {sys.argv[2]} {number2} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
