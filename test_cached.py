#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):  # self: <class Spam>; args: ('Spam', ...)
        super().__init__(*args, **kwargs)
        self._instances = weakref.WeakValueDictionary()

    def __call__(self, *args):  # self: <class Spam>, . . .
        if args in self._instances:
            return self._instances[args]
        obj = super().__call__(*args)
        self._instances[args] = obj
        return obj


class Spam(metaclass=Cached):
    """
    >>> s1 = Spam("foo", 10)
    Spam initialized
    >>> s2 = Spam("foo", 20)
    Spam initialized
    >>> s3 = Spam("foo", 10)
    >>> s1 is s3
    True
    """

    def __init__(self, msg, val):
        print("Spam initialized")
        self.msg = msg
        self.val = val

    def show(self):
        print("self.msg = {:s}, self.val = {:d}".format(self.msg, self.val))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
