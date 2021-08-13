import socket

id_addr = "127.0.0.1"
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((id_addr, port))

sock.send(b"text.txt")
sock.send(b"3")
text = b""
while True:
    data = sock.recv(1024)
    if not data:
        break
    text += data.replace(b"\r", b"")


with open("new_text.txt", "w") as file:
    file.write(text.decode("utf-8"))