#!/usr/bin/python3
import sys
import argparse

def addition_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return

    add = 0
    for i in range(1, n + 1):
        add += int(argv[i])

    print("{:d}".format(add))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('arguments', nargs='*', help='List of arguments')
    args = parser.parse_args()

    addition_arg(args.arguments)

if __name__ == "__main__":
    main()

