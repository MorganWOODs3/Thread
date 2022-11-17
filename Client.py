# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

client_socket = socket.socket()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Bonsoir")
    data = s.recv(1024)
    host = socket.gethostname()

print(f"Received {data!r}")