#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from collections import defaultdict


class Cached(type):
    _instances = defaultdict(dict)

    def __call__(cls, msg):
        meta = type(cls)  # Cached meta class
        if cls in meta._instances:
            if msg in meta._instances[cls]:
                return meta._instances[cls][msg]
        obj = super().__call__(msg)
        meta._instances[cls][msg] = obj
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
