#client.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
print('Solicita conexão')

text = input("Digite a mensagem para o server: \n(digite \"sair\" para encerrar) \n")

while (text != 'sair'): 
	s.send(text.encode())
	data = s.recv(1024)
	print ('O servidor disse: ', data.decode())
	text = input("Digite a mensagem para o server: \n(digite \"sair\" para encerrar) \n")
	
input ('Encerrando conexão')
s.close