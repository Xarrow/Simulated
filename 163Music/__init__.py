# -*- coding:utf-8 -*-
"""
version: 1.0
author: ZhangJian
site: unkonwn
software: PyCharm
file: __init__.py.py
time: 2016/9/30 15:07
"""
import logging

level = logging.DEBUG
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
datefmt = '%Y-%m-%d %H:%M'
logging.basicConfig(level=level, format=format, datefmt=datefmt)
logger = logging.getLogger(__name__)


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass