#!/usr/bin/python3
def text_indentation(text):
    """
    Prints the text with 2 new lines after each occurrence of the characters '.', '?', and ':'.
    Inputs:
    - text: a string representing the text.
    Raises:
    - TypeError: If text is not a string.
    """
    
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Loop through each character in text
    for char in text:
        print(char, end="")
        
        # Check if the current character is '.', '?', or ':'
        if char in ['.', '?', ':']:
            print("\n" * 2, end="")
    
    print()

