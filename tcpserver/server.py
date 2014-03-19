# -*- coding: utf-8 -*-

# message存在queue里, 取出处理即可

from tornado.ioloop import IOLoop
from functools import partial
from share import fd2sock, sock2queue, ioloop
import socket, Queue


def init_socket(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(addr)
    sock.listen(200)
    fd = sock.fileno()
    fd2sock[fd] = sock
    return (fd, sock)

def handle_client(fd, event, cli_addr):
    s = fd2sock[fd]
    if event & IOLoop.READ:
        data = s.recv(1024)
        if data:
            print "Recv:", data, cli_addr
            ioloop.update_handler(fd, IOLoop.WRITE)
            sock2queue[s].put(data)
        else:
            print "Closing:", cli_addr
            ioloop.remove_handler(fd)
            s.close()
            del sock2queue[s]
 
    if event & IOLoop.WRITE:
        try:
            next_msg = sock2queue[s].get_nowait()
        except Queue.Empty:
            print "Queue empty:", cli_addr
            ioloop.update_handler(fd, IOLoop.READ)
        else:
            print "Send:", next_msg, cli_addr
            s.send(next_msg)
 
    if event & IOLoop.ERROR:
        print "Exception on:", cli_addr
        ioloop.remove_handler(fd)
        s.close()
        del sock2queue[s]

def handle_server(fd, event):
    s = fd2sock[fd]
    if event & IOLoop.READ:
        conn, cli_addr = s.accept()
        conn.setblocking(0)
        conn_fd = conn.fileno()
        fd2sock[conn_fd] = conn
        handle = partial(handle_client, cli_addr=cli_addr)  
        ioloop.add_handler(conn_fd, handle, IOLoop.READ)
        sock2queue[conn] = Queue.Queue()   # 创建对应的消息队列

fd = None
sock = None

def add_handler(port, event=IOLoop.READ):
    global fd
    global sock
    fd, sock = init_socket(("0.0.0.0", port))
    handle = partial(handle_server)
    ioloop.add_handler(fd, handle, event)
    
__all__ = ["add_handler", "fd", "sock"]
        