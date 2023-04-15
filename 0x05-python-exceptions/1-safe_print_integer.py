#!/usr/bin/python3

"""safe printing integer task1"""

def safe_print_integer(value):
    try:
	print("{:d}".format(value))
	return True
    else:
         print(TypeError, ValueError):
        return False
