import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(1)

print("HTTP Server running...")

while True:
    conn, addr = server.accept()

    request = conn.recv(1024).decode()
    print("Received Request:")
    print(request)

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n"
        "\r\n"
        "<html><body>"
        "<h1>Welcome to Computer Networks Lab!</h1>"
        "</body></html>"
    )

    conn.sendall(response.encode())
    conn.close()