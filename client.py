import socketfile:///data/user/0/com.foxdebug.acodefree/files/public/client.py

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 8080))

request = (
           "GET / HTTP/1.1\r\n"
           "Host: localhost\r\n"
           "Connection: close\r\n"
           "\r\n"
)

client.sendall(request.encode())

response = b""

while True:
    data = client.recv(1024)

    if not data:
        break

    response += data

print(response.decode())

client.close()