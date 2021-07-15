import asyncio
import socket

ip_addr = "127.0.0.1"
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip_addr, port))
sock.listen(10)
conn, addr = sock.accept()

async def receive_and_return(data):
    new_data ="а может ты " + str(data)
    print(f"and i reply him {new_data}")
    conn.send(new_data.encode())

while True:
    data = conn.recv(1024)
    data = data.decode()
    print(f"someone said me {data}")
    asyncio.run(receive_and_return(data))
