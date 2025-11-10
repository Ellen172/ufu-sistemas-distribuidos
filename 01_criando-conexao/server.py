#server.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345 # normalmente usa-se: 88888
s.bind((host,port))

print('Escutando meio')
s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting'.encode())
    c.close()

