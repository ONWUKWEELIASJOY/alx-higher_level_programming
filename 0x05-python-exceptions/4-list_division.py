#!/usr/bin/python3

"""division of elements"""

def list_division(my_list_1, my_list_2, list_length):
    early_list = []
    for i in range(list_length)
        try:
            d = my_list_1[i] / my_list_2[i]
	except TypeError:
            print("wrong type")
	    d = 0
        except ZeroDivisionError:
            print("division by 0")
	    d = 0
        except IndexError:
	    print("out of range")
            d = 0
        finally:
	    early_list.append(d)
    return early_list 
