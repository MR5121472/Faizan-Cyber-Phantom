import socket
import socks  # PySocks library

class ProxyEngine:
    def __init__(self, proxy_ip='127.0.0.1', proxy_port=9050):
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port
        self.sock = None

    def start_proxy(self):
        print("[+] Initializing Faizan™ Privacy Proxy Engine...")
        # Set default SOCKS5 proxy (used by Tor)
        socks.set_default_proxy(socks.SOCKS5, self.proxy_ip, self.proxy_port)
        socket.socket = socks.socksocket
        print(f"[+] Proxy initialized through SOCKS5 at {self.proxy_ip}:{self.proxy_port}")

    def connect(self, dest_host, dest_port):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((dest_host, dest_port))
            print(f"[+] Connected to {dest_host}:{dest_port} via Tor proxy.")
            return True
        except Exception as e:
            print(f"[-] Connection failed: {e}")
            return False

    def send_data(self, data):
        if self.sock:
            self.sock.sendall(data)
            print("[+] Data sent successfully.")
        else:
            print("[-] Socket not connected.")

    def receive_data(self, buffer_size=4096):
        if self.sock:
            return self.sock.recv(buffer_size)
        else:
            print("[-] Socket not connected.")
            return None

    def close_connection(self):
        if self.sock:
            self.sock.close()
            print("[+] Connection closed.")
