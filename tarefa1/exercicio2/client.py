import socket

# Server configuration
UDP_IP = "127.0.0.1"  # Server's IP address
UDP_PORT = 5005      # Server's port
BUFFER_SIZE = 1024   # Buffer size for receiving messages
MENU = "\n\n Escolha a operação (soma(a,b), subtrai(a,b), multiplica(a,b), divide(a,b)): "

# Escolher uma operação e inserir dois valores.
option = input(MENU)

# Enviar requisição ao servidor usando RPC.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"Sending message to {UDP_IP}:{UDP_PORT}: {option}")
sock.sendto(option.encode('utf-8'), (UDP_IP, UDP_PORT))

# Mostrar resultado retornado pelo servidor.
data, addr = sock.recvfrom(BUFFER_SIZE)
reply = data.decode('utf-8')
print(f"Received reply from {addr}: {reply}")

# Close the socket
sock.close()
