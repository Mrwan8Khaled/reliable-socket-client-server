# reliable-socket-client-server

A lightweight Python TCP client/server system with **auto-reconnect support**.  
The server handles multiple clients, while the client automatically reconnects if the server goes offline.  
Perfect for learning sockets, experimenting with networking, or building a simple chat system.

---

## ✨ Features
- Multi-client server (each client handled in its own thread).
- Client auto-reconnects if:
  - The server is down when starting.
  - The server disconnects while running.
- Simple `send` and `receive` methods for communication.
- Broadcast support on the server.
- Easy to extend for chat apps, remote commands, or networking experiments.

---

## 📂 Project Structure
reliable-socket-client-server/
│── server.py # The server code <br>
│── client.py # The client code <br>
│── README.md # Documentation <br>
│── LICENSE # Open-source license <br>
│── requirements.txt # (empty for now, pure Python standard library) <br>

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Mrwan8Khaled/py-socket-chat.git
cd reliable-socket-client-serverbash
```
2. Run the server
```
python3 server.py
Server will start listening on 0.0.0.0:6000 (default).
```
3. Run the client
```
python3 client.py
The client will:

Try to connect to the server.

Retry every 5 seconds if the server is offline.

Reconnect if the server disconnects.

🖥 Example Usage
When you start the server:

[SERVER] Starting server
[SERVER] Listening on 0.0.0.0:6000
When the client connects:

[client] Connecting to 127.0.0.1:6000...
[client] Connected successfully!
If the server goes offline, the client will retry:

[client] Server disconnected.
[client] Attempting to reconnect...
```

🛠 Requirements
Python 3.x

No external dependencies (pure standard library)
