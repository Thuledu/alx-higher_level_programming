#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

def write_file(filename="", text=""):
  """Writes a string to a text file (UTF8) and returns the number of characters written.

  Args:
    filename: The name of the file to write.
    text: The string to write to the file.

  Returns:
    The number of characters written to the file.
  """

	with open(filename, "w", encoding="utf-8") as f:
		return f.write(text)
