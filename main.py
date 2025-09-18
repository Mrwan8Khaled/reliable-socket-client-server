import socket
import threading

PORT = 6000
IP = '0.0.0.0'

Socket_Clients = {}

class socketServer:
    def __init__(self, ip, port):
        print(f"[SERVER] Starting server")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((ip, port))
        self.s.listen(10)
        print(f"[SERVER] Listening on {ip}:{port}")

        while True:
            client, addr = self.s.accept()
            print(f"[SERVER *](NEW) Connection from {addr}")
            self.AddClient(client, addr)
            threading.Thread(target=self.handle_client, args=(client, addr), daemon=True).start()

    def handle_client(self, client, addr):
        try:
            client.send(b"Hello from server!\n")
            while True:
                data = client.recv(1024)
                if not data:
                    break
                print(f"[SERVER] Received from {addr}: {data.decode().strip()}")
                client.send(b"Echo: " + data)  # echo back
        except Exception as e:
            print(f"[SERVER] Error with {addr}: {e}")
        finally:
            self.DisconnectClient(addr)

    def AddClient(self, client, addr):
        Socket_Clients[addr] = client

    def RemoveClient(self, addr):
        if addr in Socket_Clients:
            del Socket_Clients[addr]

    def SendToClient(self, addr, data):
        if addr in Socket_Clients:
            client = Socket_Clients[addr]
            client.send(data)
        else:
            print(f"[SERVER] No client with address {addr}")
    
    def Broadcast(self, data):
        for addr, client in list(Socket_Clients.items()):
            try:
                client.send(data)
            except Exception as e:
                print(f"[SERVER] Error sending to {addr}: {e}")
                self.RemoveClient(addr)

    def GetClients(self):
        return list(Socket_Clients.keys())

    def IsClientConnected(self, addr):
        return addr in Socket_Clients

    def DisconnectClient(self, addr):
        if addr in Socket_Clients:
            client = Socket_Clients[addr]
            client.close()
            self.RemoveClient(addr)

def main():
    socketServer(IP, PORT)

if __name__ == "__main__":
    main()
