import socket
import string

ip_addr = "127.0.0.1"
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip_addr, port))
sock.listen(1)
conn, addr = sock.accept()

file = b""
data = conn.recv(1024)
file += data
decode = conn.recv(1024)

def coding_cesar(some_byte_str, decode: int)-> str:
    alpha = string.ascii_lowercase
    new_str = ""
    counter = 0
    for i in some_byte_str.decode():
        if i in alpha:
            new_str += alpha[alpha.index(i)+decode]
        else:
            new_str += i
        counter += 1
    return new_str

with open(file.decode("utf-8"), "rb") as text:
    while True:
        result = text.read(1024)
        result = coding_cesar(result, int(decode))
        if not result:
            conn.sendall(result.encode())
            break
        conn.sendall(result.encode())

conn.close()