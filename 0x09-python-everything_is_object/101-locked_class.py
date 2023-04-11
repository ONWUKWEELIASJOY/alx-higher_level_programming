#!/usr/bin/python3

class LockedMeta(type):
    def __new__(cls, name, bases, dct):
	dct['__slots__'] = ('first_name',)
	return
super().__new__(cls, name, bases, dct)


class LockedClass(metaclass=LockedMeta):
    """ locked class """
    pass
