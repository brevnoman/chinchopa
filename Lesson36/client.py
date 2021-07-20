import socket
import threading


HOST = '127.0.0.1'
PORT = 65432


def print_to_chat(s):
    while True:
        chat = input()
        s.send(chat.encode("utf-8"))

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            print("you always can change your name using '/rename'\n")
            username = input("write your username")
            s.send(username.encode("utf-8"))
            validate = s.recv(1024)
            if validate == b"nope":
                print("sry you can't choose this username")
            else:
                break
        threading.Thread(target=print_to_chat, args=(s,)).start()
        while True:
            data = s.recv(1024)

            if not data:
                break
            print(data.decode('utf-8'))