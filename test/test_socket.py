# -*- coding:utf-8 -*-


"""
 Verion: 1.0
 Author: zhangjian
 Site: http://iliangqunru.com
 File: test_socket.py
 Time: 2016/10/3 21:59
"""
import logging
import sys
import socket

level = logging.DEBUG
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
datefmt = '%Y-%m-%d %H:%M'
logging.basicConfig(level=level, format=format, datefmt=datefmt)
logger = logging.getLogger(__name__)


def sock_demo1():
    print socket.gethostbyname("www.baidu.com")
    print socket.getservbyport(80)


def socket_demo2():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(("localhost", 8000))
    socket_address = s.getsockname()
    print 'Trivial Server launched on socket :%s' % str(socket_address)
    s.s
    while True:
        s.listen(1)


if __name__ == '__main__':
    socket_demo2()