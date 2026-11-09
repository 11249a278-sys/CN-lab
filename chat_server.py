import socket
import threading

clients = []

def handle_client(client, address):
    print("Connected:", address)

    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print("Client:", message)

            for c in clients:
                if c != client:
                    c.sendall(message.encode())

        except:
            break

    if client in clients:
        clients.remove(client)

    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 55555))
server.listen(5)

print("Chat Server Started...")

while True:
    client, address = server.accept()

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()