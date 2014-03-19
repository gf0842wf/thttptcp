# -*- coding: utf-8 -*-

from handlers.errors import PageNotFoundHandler
from handlers.test import TestHandler

urls = [
    (r"/", TestHandler),
    
    # 在最后加一个 PageNotFoundHandler 来处理这里没有的请求(贪婪匹配,一直匹配到最后,发现没有,就调用这个handler了)
    # PageNotFoundHandler 的 get 里 raise tornado.web.HTTPError(404)即可
    (r".*", PageNotFoundHandler),
    ]

