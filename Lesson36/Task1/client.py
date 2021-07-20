import socket
import concurrent.futures


HOST = '127.0.0.1'
PORT = 65432


def print_to_chat(s):
    while True:
        chat = input()
        s.send(chat.encode("utf-8"))

def listen_chat(s):
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))

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
            elif validate == b" ":
                break
        pool = [print_to_chat, listen_chat]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for func in pool:
                executor.submit(func, s)