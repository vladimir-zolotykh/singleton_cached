#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


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
    def __init__(self, text):
        print("Spam.__init__ is called")
        self.text = text

    def show(self):
        print("self.text = {:10s}".format(self.text))


if __name__ == "__main__":
    s1 = Spam("foo")
    s2 = Spam("bar")
    s3 = Spam("baz")
    s1.show()
    s2.show()
    s3.show()
    assert s1 is s2
