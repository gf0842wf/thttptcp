# -*- coding: utf-8 -*-

import tornado.web

from handlers.base import BaseHandler

class PageNotFoundHandler(BaseHandler):
    def get(self):
        raise tornado.web.HTTPError(404)
    
    
__all__ = ["PageNotFoundHandler"]