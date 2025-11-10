#client.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
print("1")
data = s.recv(1024)
print(data.decode())
s.close()

