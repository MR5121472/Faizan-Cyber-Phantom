import time
import socket
from stem import Signal
from stem.control import Controller

def rotate_ip_via_tor():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate("/data/data/com.termux/files/usr/var/lib/tor/control_auth_cookie")
            controller.signal(Signal.NEWNYM)
            print("[✔] IP rotation signal sent to Tor.")
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
        print("[✔] Connection test successful.")
    except Exception as e:
        print(f"[!] Connection test failed: {e}")

if __name__ == "__main__":
    print("[*] Rotating IP via Tor network every 2 seconds...\n")
    for i in range(4):
        rotate_ip_via_tor()
        time.sleep(2)
