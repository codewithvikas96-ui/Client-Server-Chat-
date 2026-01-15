# server.py
import socket
import threading

clients = {}

def handle_client(sock, addr):
    try:
        username = sock.recv(1024).decode().strip()
        clients[username] = sock
        print(f"[SERVER] {username} {addr} joined the chat")

        # Notify others
        for user, client in clients.items():
            if client != sock:
                client.send(f"[SERVER] {username} joined".encode())

        while True:
            msg = sock.recv(1024)

            # Client disconnected
            if not msg:
                break

            msg = msg.decode()
            print(f"[RECEIVED] {username}: {msg}")

            # Broadcast
            for user, client in clients.items():
                if client != sock:
                    client.send(f"{username}: {msg}".encode())

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        print(f"[SERVER] {username} left the chat")
        del clients[username]
        sock.close()

        # Notify others
        for user, client in clients.items():
            client.send(f"[SERVER] {username} left".encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))
server.listen()
print("[SERVER] Started")

while True:
    client_sock, addr = server.accept()
    threading.Thread(
        target=handle_client,
        args=(client_sock, addr),
        daemon=True
    ).start()
