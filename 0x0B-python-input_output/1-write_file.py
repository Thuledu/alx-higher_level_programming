#!/usr/bin/python3
def write_file(filename="", text=""):
	with open(filename, "w", encoding="utf8") as file:
		num_chars = file.write(text)
	return num_chars
