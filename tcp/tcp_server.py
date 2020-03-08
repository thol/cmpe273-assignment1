import socket 
from thread import *
# import select
# import sys

TCP_IP      = '0.0.0.0'
TCP_PORT    = 2004
BUFFER_SIZE = 20
pong_msg    = 'Pong'

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
tcpServer.listen(100) # Max number of clients
print "Server started at port " + str(TCP_PORT)
client_threads = [] 

def ClientThread(conn, client_id): 
    print "Connected Client:" + client_id + "."
    while True :
        try:
            data = conn.recv(2048) 
            if data:
                print "Received data:" + client_id + ":" + data
                conn.send(pong_msg)
        except:
            continue
 
while True: 
    # print "Multithreaded Python server : Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer.accept()
    client_id  = conn.recv(2048)
    conn.send("ACK")
    client_threads.append(conn)
    start_new_thread(ClientThread,(conn, client_id))

conn.close()
tcpServer.close()
