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
	data = c.recv(1024)
	text = data.decode()
	while(text != 'sair'):
		print ('O cliente disse: ', text)
		resp = input('Digite a mensagem para o cliente: \n')
		c.send(resp.encode())
		data = c.recv(1024)
		text = data.decode()
	print ('Encerrando conexão')
	c.close