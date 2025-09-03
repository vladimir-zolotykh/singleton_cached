#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class _Cached(type):
    _instances = {}

    def __call__(cls, msg):
        if cls in _Cached._instances:
            if msg in _Cached._instances[cls]:
                return _Cached._instances[cls][msg]
        obj = super().__call__(msg)
        if cls not in _Cached._instances:
            _Cached._instances[cls] = dict(msg=obj)
        else:
            _Cached._instances[cls][msg] = obj
        return obj


class Spam2(metaclass=_Cached):
    """
    >>> p1 = Spam2("foo")
    Spam2 initialized
    >>> p2 = Spam2("bar")
    Spam2 initialized
    >>> p3 = Spam2("foo")
    >>> p1 is p3
    True
    """

    def __init__(self, msg):
        print("Spam2 initialized")
        self.msg = msg

    def show(self):
        print("self.msg = {:s}".format(self.msg))


class Singleton(type):
    _instances = {}  # instances of Spam class

    def __call__(cls, *args, **kwargs):
        if cls in Singleton._instances:
            return Singleton._instances[cls]
        else:
            obj = super().__call__(*args, **kwargs)
            Singleton._instances[cls] = obj
            return obj


class Spam(metaclass=Singleton):
    """
    >>> s1 = Spam("foo")
    Spam.__init__ is called
    >>> s1.show()
    self.text = foo
    >>> s2 = Spam("bar")
    >>> assert s1 is s2
    """

    def __init__(self, text):
        print("Spam.__init__ is called")
        self.text = text

    def show(self):
        print("self.text = {:s}".format(self.text))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
