import socket



ip_addr = "127.0.0.1"
port = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip_addr, port))
data, addr = sock.recvfrom(1024)
with open(data.decode("utf-8"), "rb") as text:
    while True:
        result = text.read(1024)
        if not result:
            sock.sendto(result, addr)
            break
        sock.sendto(result, addr)



sock.close()