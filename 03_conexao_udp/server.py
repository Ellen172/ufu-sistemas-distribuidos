import socket

# Server configuration
UDP_IP = "127.0.0.1"  # Localhost
UDP_PORT = 5005      # Port to listen on
BUFFER_SIZE = 1024   # Buffer size for receiving messages

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port
sock.bind((UDP_IP, UDP_PORT))

print(f"UDP server listening on {UDP_IP}:{UDP_PORT}")

while True:
    # Receive data and address
    data, addr = sock.recvfrom(BUFFER_SIZE)

    # Decode the received message
    message = data.decode('utf-8')

    print(f"Received message from {addr}: {message}")

    # Send a reply back to the client
    reply_message = "Hello from UDP server!"
    sock.sendto(reply_message.encode('utf-8'), addr)
    print(f"Sent reply to {addr}")
