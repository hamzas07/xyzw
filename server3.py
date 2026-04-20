import socket
import threading

clients = []

def handle_client(conn, addr):
    print(f"Client {addr} joined the group")
    clients.append(conn)

    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                print(f"Message from {addr}: {message}")
                broadcast(message, conn)
        except:
            clients.remove(conn)
            conn.close()
            break


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8283))
server.listen()

print("Group Communication Server running on port 9000...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()