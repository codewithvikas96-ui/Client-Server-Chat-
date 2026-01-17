# 🖥️ Multiple Client Chat Application (Python)  

![Python](https://img.shields.io/badge/Python-3.x-blue)   ![Socket](https://img.shields.io/badge/Socket-TCP%2FUDP-green)

A simple socket-based chat application that supports multiple clients connecting to a server.

---

## 🚀 Features
- Multiple clients can connect simultaneously
- Real-time message broadcasting
- Username-based identification
- Simple and lightweight (uses only Python standard library)

---

## 📂 Repository Structure
- `server.py` → Chat server
- `client.py` → Chat client
- `README.md` → Documentation

---

## ⚙️ How to Run

### 1. Start the Server
```bash
python server.py
```
### 2. Start Clients
```bash
python client.py
```
`You can run multiple clients in separate terminals.`
#### Note: Start the server first then run the clients
---

## 📝 Usage
- Enter a username when prompted.
- Type a message and press Enter to send.
- Messages are broadcast to all connected clients.
- Type exit to disconnect.

---

## 📖 Understanding the socket Module
The socket module in Python provides low-level networking interfaces. It allows programs to communicate over networks using protocols like TCP and UDP.

### 🔑 Key Concepts
- **Socket:** An endpoint for sending or receiving data across a network.
- **Server Socket:** Listens for incoming connections (`bind`, `listen`, `accept`).
- **Client Socket:** Initiates a connection to the server (`connect`).
- **TCP vs UDP:**
  - **TCP (SOCK_STREAM) →** Reliable, connection-oriented communication.
  - **UDP (SOCK_DGRAM) →** Faster, connectionless communication.

### ⚙️ Common Functions
- `socket.socket(family, type)` → Creates a new socket.
- `bind(address)` → Associates the socket with a local address.
- `listen()` → Puts the server socket into listening mode.
- `accept()` → Accepts a new connection from a client.
- `connect(address)` → Connects a client socket to a server.
- `send(data) / recv(buffer_size)` → Send and receive data.
- `close()` → Closes the socket.

### 📌 Example
```python
import socket

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
s.connect(("localhost", 12345))

# Send data
s.send(b"Hello, Server!")

# Receive response
print(s.recv(1024).decode())

# Close connection
s.close()
```

### 🧠 Why socket Matters
- Forms the backbone of network programming in Python.
- Used in chat apps, web servers, IoT devices, and more.
- Provides flexibility to build custom communication protocols.

---

## 🔮 Future Improvements
- Add private messaging between users.
- GUI using Tkinter or PyQt.
- Encryption for secure communication.
- Persistent chat logs

---
