#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):  # self: <class Spam>; args: ('Spam', ...)
        super().__init__(*args, **kwargs)
        self._instances = weakref.WeakValueDictionary()

    def __call__(self, msg):  # self: <class Spam>, msg: "foo"
        if msg in self._instances:
            return self._instances[msg]
        obj = super().__call__(msg)
        self._instances[msg] = obj
        return obj


class Spam(metaclass=Cached):
    """
    >>> s1 = Spam("foo")
    Spam initialized
    >>> s2 = Spam("bar")
    Spam initialized
    >>> s3 = Spam("foo")
    >>> s1 is s3
    True
    """

    def __init__(self, msg):
        print("Spam initialized")
        self.msg = msg

    def show(self):
        print("self.msg = {:s}".format(self.msg))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
