import socket
import threading
import datetime


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
            conn.settimeout(600)
            self.clients.append(conn)

            threading.Thread(target=self.listen_to_client, args=(conn, address)).start()

    def rename(self, conn, old_name):
        while True:

            username = conn.recv(1024).decode("utf-8")
            if username in self.clients_names:
                conn.send(b"nope")
            else:
                conn.send(b" ")
                self.clients_names.append(username)
                for client in self.clients:
                    client.send(f"{old_name} changed his/her name to {username}".encode("utf-8"))
                with open("chat_story.txt", "a") as file:
                    file.write(f"{old_name} changed his/her name to {username}\n")
                self.clients_names.remove(old_name)
                return username

    def validate_user(self, conn):
        while True:
            username = conn.recv(1024).decode("utf-8")
            if username in self.clients_names:
                conn.send(b"nope")
            else:
                conn.send(b" ")
                self.clients_names.append(username)
                for client in self.clients:
                    client.send(f"{username} joined chat".encode("utf-8"))
                with open("chat_story.txt", "a") as file:
                    file.write(f"{username} joined chat\n")
                return username

    def listen_to_client(self, conn, address):
        print(f"[{datetime.datetime.now()}]", address[0] + ":" + str(address[1]), " connected")
        size = 1024
        username = self.validate_user(conn)
        print(f"[{datetime.datetime.now()}]", address[0] + ":" + address[1], f" got {username} name")
        with open("chat_story.txt", "r") as old_file:
            conn.send(old_file.read().encode("utf-8"))

        while True:
            try:
                data = conn.recv(size).decode('utf-8')
                
                if data:
                    if data == "/rename":
                        conn.send("choose new name".encode("utf-8"))
                        username = self.rename(conn, username)
                    else:
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