#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Singleton(type):
    _instances = []

    def __call__(self, *args, **kwargs):
        print(f"{Singleton._instances = }")
        if self in Singleton._instances:
            return self
        else:
            obj = super().__call__(*args, **kwargs)
            Singleton._instances.append(obj)
            return obj


class Spam(metaclass=Singleton):
    def __init__(self, text):
        print("Spam.__init__ is called")
        self.text = text

    def show(self):
        print(f"{self.text = }")


if __name__ == "__main__":
    s1 = Spam("foo")
    s2 = Spam("foo")
    s1.show()
    s2.show()
    # assert s1 is s2
