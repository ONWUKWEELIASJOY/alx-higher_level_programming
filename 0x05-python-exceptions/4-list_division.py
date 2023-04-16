#!/usr/bin/python3

"""This function takes in 3 parameters: my_list_1, my_list_2, and list_length."""

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
             raise IndexError("out of range")
            result = my_list_1[i] / my_list_2[i]
new_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
new_list.append(0)
        except TypeError:
            print("wrong type")
new_list.append(0)
        except IndexError as e:
            print(e)
            return
        finally:
            continue
                return new_list

