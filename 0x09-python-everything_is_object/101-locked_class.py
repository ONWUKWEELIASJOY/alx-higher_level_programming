#!/usr/bin/python3

class LockedClass:
locked class
  def __setattr__(self, name, value):
    if not hasattr(self, name):
       object.__setattr__(self, name, value)
    else:
      raise AttributeError(f"{name} attribute is locked and cannot be set")

# available slots that can be created
__slots__ = ('first_name',)

"""
An OOP task on alx,)
"""
