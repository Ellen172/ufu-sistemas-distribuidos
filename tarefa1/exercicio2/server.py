import socket

# Server configuration
UDP_IP = "127.0.0.1"  # Localhost
UDP_PORT = 5005      # Port to listen on
BUFFER_SIZE = 1024   # Buffer size for receiving messages

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"UDP server listening on {UDP_IP}:{UDP_PORT}")

# O servidor deve permanecer ativo, atendendo múltiplas requisições de clientes.
while True:

    # Recebe mensagem do cliente
    data, addr = sock.recvfrom(BUFFER_SIZE)
    message = data.decode('utf-8')
    print(f"Received message from {addr}: {message}")

    resultado = "Nenhuma mensagem."

    if message: 
        
        partes = message.replace(')', '').split('(')
        nome_funcao = partes[0].strip()  # "tipo de operação"
        
        argumentos = partes[1].split(',')
        variavel_a = argumentos[0].strip() # "variavel a"
        variavel_b = argumentos[1].strip() # "variavel b"

        if nome_funcao == "soma": 
            resultado = int(variavel_a) + int(variavel_b)

        if nome_funcao == "subtrai":
            resultado = int(variavel_a) - int(variavel_b)

        if nome_funcao == "multiplica":
            resultado = int(variavel_a) * int(variavel_b)

        if nome_funcao == "divide":
            resultado = int(variavel_a) / int(variavel_b)

    # Envia Resposta
    sock.sendto(str(resultado).encode('utf-8'), addr)
    print(f"Sent reply to {addr}")
