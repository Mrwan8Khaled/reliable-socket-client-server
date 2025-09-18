import socket
import threading
import time

SOCKET = ("corporate-elephant.gl.at.ply.gg", 49338)

class socketClient:
    def __init__(self):
        self.sock = None
        self.connected = False
        self.connect()

    def connect(self, scoket=SOCKET):
        while not self.connected:
            try:
                print(f"[client] Connecting to {scoket[0]}:{scoket[1]}...")
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect(scoket)
                self.connected = True
                print("[client] Connected successfully!")
                threading.Thread(target=self.receive, daemon=True).start()
            except Exception as e:
                self.connected = False
                print(f"[client] Connection failed: {e}, retrying in 5s...")
                time.sleep(5)

    def send(self, data: str):
        try:
            self.sock.sendall(data.encode() + b"\n")
        except Exception as e:
            print(f"[client] Send failed: {e}")
            self.reconnect()

    def receive(self):
        try:
            while True:
                data = b""
                while not data.endswith(b"\n"):
                    chunk = self.sock.recv(4096)
                    if not chunk:
                        print("[client] Server disconnected.")
                        self.reconnect()
                        return
                    data += chunk
                print("[client] Received:", data.decode().strip())
        except Exception as e:
            print(f"[client] Error in receive: {e}")
            self.reconnect()

    def reconnect(self):
        if self.sock:
            try:
                self.sock.close()
            except:
                pass
        self.connected = False
        print("[client] Attempting to reconnect...")
        self.connect()

    def close(self):
        self.connected = False
        if self.sock:
            self.sock.close()

def main():
    client = socketClient()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()