import socket
from socket import timeout

# Server configuration
UDP_IP = "127.0.0.1"  # Server's IP address
UDP_PORT = 5005      # Server's port
BUFFER_SIZE = 1024   # Buffer size for receiving messages
TIMEOUT_SECONDS = 1.0 # O tempo que você quer esperar

MENU = "\n\n=============== Choose: \n1-Send message \n2-View new messages \n0-Exit \n"

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o timeout
sock.settimeout(TIMEOUT_SECONDS)

# input menu
menu = input(MENU)

while menu != "0":

    # Send message
    if menu == "1": 
        # Message to send
        message = input("Input message: ")

        # Send the message to the server
        sock.sendto(message.encode('utf-8'), (UDP_IP, UDP_PORT))

        # Receive a reply from the server
        data, addr = sock.recvfrom(BUFFER_SIZE)

        # Decode the received reply
        reply = data.decode('utf-8')

        print(f"Received reply from {addr}: {reply}")

    # View new messages
    if menu == "2":

        try:
            # A execução vai esperar por no máximo 1 segundo
            data, addr = sock.recvfrom(BUFFER_SIZE)
            print(f"Dados recebidos de {addr}: {data.decode()}")

        except timeout:
            # Este bloco é executado se o tempo limite for atingido
            print("Nenhuma nova mensagem")
            # Você pode adicionar aqui o código para sair do loop ou tentar novamente
            
        except Exception as e:
            # Para capturar outros erros inesperados
            print(f"Ocorreu um erro: {e}")

    # input menu
    menu = input(MENU)

# Close the socket
sock.close()
