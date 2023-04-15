 #!/usr/bin/python3

"""This function will try to print the given value as an integer using "{:d}".format().
If the value can be formatted as an integer, it will be printed followed by a new line, and the function will return True.
If the value can't be formatted as an integer, the function will return False."""


def safe_print_integer(value):
    try:

        print("{:d}".format(value))
        return True
    except:
        return False
