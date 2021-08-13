import socket


id_addr = "127.0.0.1"
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((id_addr, port))

while True:
    choose = input("write something")
    sock.send(choose.encode())
    data = sock.recv(1024)
    print(data.decode())