# 🖥️ Multiple Client Chat Application (Python)

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
- <strong>Socket:</strong> An endpoint for sending or receiving data across a network.
- <strong>Server Socket:</strong> Listens for incoming connections (`bind`, `listen`, `accept`).
- <strong>Client Socket:</strong> Initiates a connection to the server (`connect`).
- <strong>TCP vs UDP:</strong>
        - <strong>TCP (SOCK_STREAM) →</strong> Reliable, connection-oriented communication.
        - <strong>UDP (SOCK_DGRAM) →</strong> Faster, connectionless communication.
