import socket
import threading

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                print("[SERVER CLOSED CONNECTION]")
                break
            print(msg)
        except:
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

username = input("Enter username: ").strip()
client_socket.send(username.encode())

threading.Thread(
    target=receive,
    args=(client_socket,),
    daemon=True
).start()

while True:
    msg = input()

    if msg.lower() == "exit":
        print("[YOU LEFT THE CHAT]")
        client_socket.close()
        break

    client_socket.send(msg.encode())
