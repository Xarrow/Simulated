# -*- coding:utf-8 -*-
"""
version: 1.0
author: ZhangJian
site: unkonwn
software: PyCharm
file: test_decorate.py
time: 2016/9/28 17:29
"""


def func():
    pass


class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return "%s,%s" % (self.first_name, self.last_name)


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    p = Person('zhang', 'san')
    print __name__
