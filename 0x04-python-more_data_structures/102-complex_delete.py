#!/usr/bin/python3
def complex_delete(a_dictionary, value):
	new_dictionary = {key: val for key, val in a_dictionary.items() if val != value}
	a_dictionary.clear()
	return a_dictionary
