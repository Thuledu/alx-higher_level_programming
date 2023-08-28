#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	count = 0
	try:
		for element in my_list:
			if count < x:
				try:
					print("{:d}".format(element), end=" ")
					count += 1
				except ValueError:
					pass
			else:
				break
	except:
		raise Exception("Exception occurred. x is greater than the length of my_list.")
	print()
	return count
