import socket


ip_addr = "127.0.0.1"
port = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b"text.txt", (ip_addr, port))
text = b""
while True:
    print("hi")
    data = sock.recv(1024)
    print(data)
    if not data:
        break
    text += data.replace(b"\r", b"")


with open("new_text.txt", "wb") as file:
    file.write(text)
