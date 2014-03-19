# -*- coding: utf-8 -*-

from handlers.base import BaseHandler


class TestHandler(BaseHandler):
    
    def get(self):
        self.write("Hello!!")
    
__all__ = ["TestHandler"]