#!/bin/bash/python3

"a function that prints an interger"

import sys

def safe_print_integer_err(value):

    try:
        val = int(value)

        print("{:d}".format(val))
        return True
    except Exception as e:
sys.stderr.write("Exception: {}\n".format(e))
        return False
