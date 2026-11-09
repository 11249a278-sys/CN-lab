import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 12345))
server.listen(1)

print("Server listening...")

conn, addr = server.accept()

filename = conn.recv(1024).decode()

print("Receiving:", filename)

with open("received_" + filename, "wb") as file:
    while True:
        data = conn.recv(1024)

        if not data:
            break

        file.write(data)

print("File received successfully")

conn.close()
server.close()