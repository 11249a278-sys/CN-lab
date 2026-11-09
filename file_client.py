import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 12345))

filename = input("Enter filename: ")

if not os.path.isfile(filename):
    print("File not found")
    client.close()
else:
    client.sendall(filename.encode())

    with open(filename, "rb") as file:
        while True:
            data = file.read(1024)

            if not data:
                break

            client.sendall(data)

    print("File sent successfully")

    client.close()