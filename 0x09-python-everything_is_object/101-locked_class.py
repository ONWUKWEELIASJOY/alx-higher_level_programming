#!/usr/bin/python3
locked_class.py
"""This module defines a LockedClass that allows only the 'first_name' attribute to be set."""

locked_obj = LockedClass()
locked_obj.first_name = 'John'  # Allowed
locked_obj.last_name = 'Doe'    # Raises AttributeError

class LockedClass:
    """
    A locked class that allows only the 'first_name' attribute to be set.
    """
   
    def __setattr__(self, name, value):
    """
Sets the value of the specified attribute, if it is allowed.
    """
    Args:
	name (str): The name of the attribute to set.
        value (any): The value to set the attribute to.
        
    Raises:
AttributeError: If the specified attribute is not allowed to be set.
      
      if name == 'first_name':
object.__setattr__(self, name, value)
                                 elif hasattr(self, name):
object.__setattr__(self, name, value)
	                         else:
				     raise AttributeError(f"'{name}' attribute is locked and cannot be set")
"""
An OOP task on alx,)
"""
