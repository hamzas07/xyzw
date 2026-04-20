import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8283))

print("Connected to Group Server")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print("\nGroup Message:", message)
        except:
            break


thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    msg = input("Enter message: ")
    client.send(msg.encode())