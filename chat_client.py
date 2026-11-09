import socket
import threading

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print("\nMessage:", message)

        except:
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 55555))

print("Connected to Chat Server")

thread = threading.Thread(
    target=receive_messages,
    args=(client,),
    daemon=True
)

thread.start()

while True:
    message = input("You: ")

    if message.lower() == "exit":
        break

    client.sendall(message.encode())

client.close()