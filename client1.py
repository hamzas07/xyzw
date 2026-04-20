import socket
# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server
client_socket.connect(('localhost', 8281))
# Send message
client_socket.send("Hello from Client".encode())
# Receive response
data = client_socket.recv(1024).decode()
print("Message from server:", data)
client_socket.close()