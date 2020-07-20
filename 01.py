"""
server
"""
#IO并发select
# from socket import *
# from select import *
#
# ADDR = (("0.0.0.0",8888))
#
# tcp_sock = socket()
# tcp_sock.bind(ADDR)
# tcp_sock.listen(5)
#
# tcp_sock.setblocking(False)
#
# rlist = [tcp_sock]
# wlist = []
# xlist = []
#
# while True:
#     rs,ws,xs = select(rlist,wlist,xlist)
#     for r in rs:
#         if r is tcp_sock:#监听套接字
#             connfd,addr = r.accept()
#             print("connect from: ...")
#             connfd.setblocking(False)
#             rlist.append(connfd)
#
#         else:#连接套接字
#             data = r.recv(1024)
#             if not data:
#                 r.close()
#                 rlist.remove(r)
#                 continue
#             else:
#                 print(data.decode())
#                 r.send(b"OK")

#IO并发pool
from socket import *
from select import *

ADDR = (("0.0.0.0",8888))

tcp_sock = socket()
tcp_sock.bind(ADDR)
tcp_sock.listen(5)

tcp_sock.setblocking(False)

p = poll()#创建poll对象
p.register(tcp_sock,POLLIN)#关注IO对象，后面是对象的类型
map = {tcp_sock.fileno():tcp_sock}

while True:
    events = p.poll()#监控IO对象，满足条件就会有返回值，返回值是列表套元组
    for fd,event in events:
        if fd == tcp_sock.fileno():
            connfd,addr = map[fd].accept()
            print("connect from: ...")
            connfd.setblocking(False)
            p.register(connfd,POLLIN)
            map[connfd.fileno()]=connfd
        else:
            data = map[fd].recv(1024)
            if not data:
                p.unregister(fd)
                del map[fd]
                continue
            else:
                print("客户端发送的数据是:%s"%data.decode())
                map[fd].send(b"OK")

