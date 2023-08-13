#!/usr/bin/python3
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('arguments', nargs='*', help='List of arguments')
    args = parser.parse_args()

    size = len(args.arguments)

    if size > 1:
        print(f"{size} arguments:")
        for i, arg in enumerate(args.arguments, 1):
            print(f"{i}: {arg}")

    elif size == 0:
        print(f"{size} arguments.")

    else:
        print(f"{size} argument:")
        print(f"{size}: {args.arguments[0]}")

if __name__ == "__main__":
    main()
