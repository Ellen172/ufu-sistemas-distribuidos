import socket

# Server configuration
UDP_IP = "127.0.0.1"  # Localhost
UDP_PORT = 5005      # Port to listen on
BUFFER_SIZE = 1024   # Buffer size for receiving messages

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create array clients
clients = []

# Bind the socket to the IP address and port
sock.bind((UDP_IP, UDP_PORT))
print(f"UDP server listening on {UDP_IP}:{UDP_PORT}")

message = "No messages"

while True:

    # Receive data and address
    data, addr = sock.recvfrom(BUFFER_SIZE)
    
    # add addr to the clients list
    if addr not in clients:
        clients.append(addr)

        # print clients
        print("Clientes conectados: ")
        for i in clients: 
            print(f"{i},")

    # Decode the received message
    message = data.decode('utf-8')
    print(f"Received message from {addr}: \n{message}")

    # Send message to others 
    if clients:
        confirm = "\nMessagem enviada para: "
        for i in clients: 
            if i == addr: 
                continue # não envia para ele mesmo
            else: 
                sock.sendto(message.encode('utf-8'), i)
                confirm += f"\nCliente {i}"
                print(f"Sent message to {i}")
    else: 
        confirm = "No clients connected"
        print(confirm)

    # Send a reply back to the client
    sock.sendto(confirm.encode('utf-8'), addr)
    print(f"Sent reply to {addr}")

