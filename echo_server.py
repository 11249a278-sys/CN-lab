import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 65432))
server.listen(1)

print("Server listening...")

conn, addr = server.accept()

print("Connected:", addr)

while True:
    data = conn.recv(1024)

    if not data:
        break

    print("Received:", data.decode())

    conn.sendall(data)

conn.close()
server.close()