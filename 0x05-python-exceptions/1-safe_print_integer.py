 #!/usr/bin/python3

"""safe printing integer task1"""

def safe_print_integer(value):
    try:
	print("{:d}".format(value))
	return True
    else:
    except (ValueError, TypeError):
        return False
