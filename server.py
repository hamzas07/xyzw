import socket
# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind socket to localhost and port
server_socket.bind(('localhost', 8281))
# Listen for client
server_socket.listen(1)
print("Server is waiting for connection...")
conn, addr = server_socket.accept()
print("Connected to:", addr)
# Receive message
data = conn.recv(1024).decode()
print("Message from client:", data)
# Send response
conn.send("Hello from Server".encode())
conn.close()
server_socket.close()
