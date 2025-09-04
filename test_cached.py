#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Cached(type):
    _instances = {}

    def __call__(cls, msg):
        if cls in Cached._instances:
            grp = Cached._instances[cls]
            if msg in grp:
                return grp[msg]
            else:
                obj = super().__call__(msg)
                grp[msg] = obj
                return obj
        else:
            obj = super().__call__(msg)
            Cached._instances[cls] = dict(msg=obj)
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
