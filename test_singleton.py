#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Singleton(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance:
            return self._instance
        else:
            obj = super().__call__(*args, **kwargs)
            self._instance = obj
            return obj


class Spam(metaclass=Singleton):
    """
    >>> s1 = Spam()
    Spam initialized
    >>> s2 = Spam()
    >>> assert s1 is s2
    """

    def __init__(self):
        print("Spam initialized")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
