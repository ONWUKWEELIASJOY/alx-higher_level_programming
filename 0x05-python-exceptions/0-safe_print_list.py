#!/usr/bin/python3

"""This function takes a list `my_list` and a number `x` as input parameters. It then prints the first `x` elements of `my_list` if they exist, and returns the real number of elements printed.The `count` variable is used to keep track of the number of elements printed. We loop through the first `x` indices of `my_list` using a for loop, and try to print each element. If the list doesn't have an element at a certain index, an `IndexError` is thrown, and we catch it with a `try: / except:` block."""

def safe_print_list(my_list=[], x=0):
	count = 0
	for k in range(x):
            try:

	       print(my_list[i], end="")
	       count += 1
	       except IndexError:
	           break
	print()
	return count
