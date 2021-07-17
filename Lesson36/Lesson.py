import socket
import threading
import time


class ThreadedServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.clients= []
        self.clients_names = ["jojo"]

    def listen(self):
        self.sock.listen(5)
        while True:
            conn, address = self.sock.accept()
            conn.settimeout(60)
            self.clients.append(conn)
            threading.Thread(target=self.listen_to_client, args=(conn, address)).start()

    def validate_user(self, conn):
        while True:
            username = conn.recv(1024).decode("utf-8")
            if username in self.clients_names:
                conn.send(b"nope")
            else:
                conn.send(b'yeah')
                username = conn.recv(1024).decode("utf-8")
                self.clients_names.append(username)
                return username


    def listen_to_client(self, conn, address):
        print("some_shit")
        size = 1024
        username = self.validate_user(conn)
        with open("chat_story.txt", "r") as old_file:
            conn.send(old_file.read().encode("utf-8"))

        while True:
            try:
                data = conn.recv(size).decode('utf-8')
                
                if data:

                    for client in self.clients:
                        if conn == client:
                            pass
                        else:
                            client.send(f"{username} : {data}".encode("utf-8"))
                        with open("chat_story.txt", "a") as file:
                            file.write(f"{username} : {data}\n")
                        
                else:
                    raise Exception("Ni")
            except Exception:
                self.clients_names.remove(username)
                conn.close()
                return False

if __name__ == '__main__':
    serv = ThreadedServer('127.0.0.1', 65432)
    serv.listen()