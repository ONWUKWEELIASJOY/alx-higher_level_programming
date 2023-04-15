 #!/usr/bin/python3

"""safe printing interger"""

def safe_print_integer(value):
    try:
	print("{:d}".format(value))
        return True
    except:
        return False
