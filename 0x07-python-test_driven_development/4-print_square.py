#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with the character '#' of the given size.
    Inputs:
    - size: an integer representing the size length of the square.
    Raises:
    - TypeError: If size is not an integer or a float (and less than 0).
    - ValueError: If size is less than 0.
    """
    
    # Check if size is an integer
    if not isinstance(size, int):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer or a float")
    
    # Check if size is >= 0
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # Print the square
    for _ in range(size):
        print("#" * size)


# Testing the function
print_square(5)

