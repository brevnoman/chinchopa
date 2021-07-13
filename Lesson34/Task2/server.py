import concurrent.futures
import socket
import threading

"""
нужно добавить отдельную переменную для каждого потока,
потому что вывод информации бывает крайне некоректным из-за многопоточности
"""

thread_local = threading.local()

ip_addr = "127.0.0.1"
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip_addr, port))
sock.listen(10)
conn, addr = sock.accept()

def receive_and_return(data):
    new_data = "а может ты " + str(data)
    print(f"and i reply him {new_data}")
    conn.send(new_data.encode())

while True:
    data = conn.recv(1024)
    data = data.decode()
    print(f"someone said me {data}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(receive_and_return, data)


