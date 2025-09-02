#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class NoInstance(type):
    def __call__(self, *args, **kwargs):
        print(f"{self.__class__ = }, {args = }, {kwargs = }")
        raise TypeError("Can't instantiate directly")


class Spam(metaclass=NoInstance):
    def __init__(self, *args, **kwargs):
        print("Spam initialized")

    @classmethod
    def grok(cls):
        print("Spam.grok is called")


if __name__ == "__main__":
    Spam.grok()
    Spam()
