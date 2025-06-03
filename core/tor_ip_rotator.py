import time
import socket
from stem import Signal
from stem.control import Controller

def rotate_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  # CookieAuthentication by default
            controller.signal(Signal.NEWNYM)
            print("[✔] Tor IP rotation signal sent successfully.")
    except Exception as e:
        print(f"[!] Tor IP rotation failed: {e}")
        print("[-] FAILED TO CONNECT. PLEASE CHECK TOR CONTROLPORT OR torrc CONFIG.")

def test_current_ip():
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect(("check.torproject.org", 80))
        s.send(b"GET / HTTP/1.1\r\nHost: check.torproject.org\r\n\r\n")
        response = s.recv(1024)
        s.close()
        print("[✔] Connection test successful. TOR is likely working.")
    except Exception as e:
        print(f"[!] Connection test failed: {e}")
