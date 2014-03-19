# -*- coding: utf-8 -*-

import tornado.web
import json

# import urlparse

class BaseHandler(tornado.web.RequestHandler):
    repr = property(lambda self: self.request.connection.stream.socket.getpeername())
    # 对于query string类型的请求数据存在这里
#     qsbody = property(lambda self: urlparse.parse_qs(self.request.body))
    
    # 原始的
    raw = property(lambda self: self.request.body)
    
    @property
    def jsonbody(self):
        """json格式的
        """
        try:
            return json.loads(self.raw)
        except:
            self.msg("jsonbody error!")
            return ""
        
    @property
    def reqbody(self):
        """包括query string类型, 文件和headers
        """
        data = {}
        # 获得所以输入参数,并存在data中
        args = self.request.arguments
        for item in args:
            data[item] = self.get_argument(item)
        # 获取file类型参数
        data["files"] = self.request.files
        # 获取headers
        data["headers"] = self.request.headers
        return data
    
    
__all__ = ["BaseHandler"]