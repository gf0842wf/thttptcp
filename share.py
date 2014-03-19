# -*- coding: utf-8 -*-

# 共享对象

# import weakref
from tornado.ioloop import IOLoop

ioloop = IOLoop.instance()
fd2sock = {}     # fd到socket的映射
sock2queue = {}  # socket到queue的映射


__all__ = ["fd2sock", "sock2queue", "ioloop"]