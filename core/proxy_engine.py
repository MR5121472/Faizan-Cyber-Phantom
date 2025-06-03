import socket
import socks
import time
import random
from config.settings import TOR_PROXY, ROTATION_INTERVAL

class ProxyEngine:
    def __init__(self):
        self.ip_list = [
            "185.32.1.11",
            "192.168.44.1",
            "104.21.77.245",
            "172.217.14.206",
            "218.212.99.93",
            "34.67.26.126",
            "161.243.15.218",
            "24.26.97.83"
        ]

    def start_proxy(self):
        print("[+] Initializing Faizan\u2122 Privacy Proxy Engine...", flush=True)
        print("[+] Proxy Engine started in Lite Mode (No external libs)", flush=True)
        self.simulate_ip_rotation()

    def simulate_ip_rotation(self):
        print("[*] Starting IP rotation simulation every 2 seconds...\n")
        for ip in random.sample(self.ip_list, 4):
            time.sleep(ROTATION_INTERVAL)
            print(f"[\u2714] IP changed to: {ip}", flush=True)
        print("\n[\u2713] IP rotation simulation complete.\n")

    def connect(self, host, port):
        try:
            ip, port = TOR_PROXY.split(":")
            socks.setdefaultproxy(socks.SOCKS5, ip, int(port))
            socket.socket = socks.socksocket
            s = socket.socket()
            s.settimeout(10)
            s.connect((host, port))
            s.close()
            return True
        except Exception as e:
            return False

