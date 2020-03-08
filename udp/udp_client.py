import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
upload_file='./upload.txt'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Connected to the server.")
err_count=0

def send(line="ping"):
    try:
        s.sendto(line.encode(), (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        print("Received ack({})".format(data))
    except socket.error:
        err_count += 1
        print("Error! {}".format(socket.error))
        exit()

print("Starting a file ({}) upload...".format(upload_file))
with open(upload_file) as f:
    for line in f.readlines():
        send(line)

s.close()
print("Error count {}".format(err_count))
print("File upload successfully completed.")