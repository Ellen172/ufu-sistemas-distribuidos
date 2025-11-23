import socket

# Server configuration
UDP_IP = "127.0.0.1"  # Server's IP address
UDP_PORT = 5005      # Server's port
BUFFER_SIZE = 1024   # Buffer size for receiving messages

# Message to send
MESSAGE = "Hello, UDP Server!"

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the message to the server
print(f"Sending message to {UDP_IP}:{UDP_PORT}: {MESSAGE}")
sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))

# Receive a reply from the server
data, addr = sock.recvfrom(BUFFER_SIZE)

# Decode the received reply
reply = data.decode('utf-8')

print(f"Received reply from {addr}: {reply}")

# Close the socket
sock.close()
