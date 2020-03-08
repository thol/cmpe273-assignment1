# Python TCP Client A
import socket
import time
import sys

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2048
ping_msg = 'ping'

if len(sys.argv) == 4:
    client_id   = str(sys.argv[1])
    sleep_delay = int(sys.argv[2])
    ping_count  = int(sys.argv[3])
else:
    print "Usage tcp_client.py [client id] [delay in seconds between messages] [number of 'ping' messages]"
    exit()
 
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClient.connect((host, port))
tcpClient.send(client_id)
data = tcpClient.recv(BUFFER_SIZE)

for num in range(ping_count):
    tcpClient.send(ping_msg)
    data = tcpClient.recv(BUFFER_SIZE)
    print "Received data:", data
    time.sleep(sleep_delay)

tcpClient.close() 
