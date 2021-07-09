import multiprocessing
import socket

ip_addr = "127.0.0.1"
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip_addr, port))
sock.listen(10)
conn, addr = sock.accept()

def receive_and_return(data):
    new_data = "сам ты " + data
    conn.send(new_data.encode())

while True:
    data = conn.recv(1024)
    data = data.decode()
    print(f"someone said me {data}")
    process = multiprocessing.Process(target=receive_and_return(data))
