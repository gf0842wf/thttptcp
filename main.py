# -*- coding: utf-8 -*-

"""启动web server"""

import logging

from application import application
from tornado.options import define, options

# tornado没有的命令要通过define定义(logging等命令有了)
define("httpport", 8880, help="define http port", type=int)
define("tcpport", 8881, help="define tcp port", type=int) 

        
if __name__ == "__main__":
    options.logging = "debug"           # *1
    options.log_file_prefix = "var/log/test_log@8880_8881.log"
    options.parse_command_line()
    from share import ioloop
    from tcpserver.server import add_handler
    # 启动http服务
    application.listen(options.httpport)
    logging.debug("http server:%s", options.httpport)
    # 启动tcp服务
    add_handler(options.tcpport)
    logging.debug("tcp server:%s", options.tcpport)
    # IO 循环
    ioloop.start()
    # python main.py --httpport=8880 --tcpport=8881 --logging=warning  # 这里的会覆盖 *1行的
