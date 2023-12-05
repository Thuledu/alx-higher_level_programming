#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout."""

def read_file(filename=""):
  """Prints the contents of a text file to stdout.
  Args:
    filename: The name of the file to read.
  """
	with open(filename, "r", encoding="utf-8") as f:
		print(f.read())
