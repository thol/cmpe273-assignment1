import socket
import time
import hashlib


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024

def listen_for_clients():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print("Server started at port {}".format(UDP_PORT))

    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        m = hashlib.md5()
        m.update(data)
        # print("{}: {}".format(ip, data.strip()))
        # print(m.hexdigest())
        # reply back to the client
        s.sendto(m.hexdigest().encode(), ip)


listen_for_clients()