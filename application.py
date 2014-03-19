# -*- coding: utf-8 -*-

"""settings"""

from urls import urls

import tornado.web
import os

get_path = lambda d: os.path.join(os.path.dirname(__file__), d)
SETTINGS = dict(
    template_path=get_path("templates"),
    static_path=get_path("static"),
    cookie_secret="6de683f6e8f038f62863fe27a17573e5",
#     debug=True,
    )

application = tornado.web.Application(
    handlers=urls,
    **SETTINGS
    )
