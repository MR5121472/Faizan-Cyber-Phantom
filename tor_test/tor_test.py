import socks
import socket

def test_tor_connection():
    print("🌐 Testing Tor Proxy Connection via SOCKS5")

    # Set Tor SOCKS proxy
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

    try:
        # Connect to example IP checker
        sock = socket.socket()
        sock.connect(("check.torproject.org", 80))
        sock.sendall(b"GET / HTTP/1.1\r\nHost: check.torproject.org\r\n\r\n")
        response = sock.recv(4096)
        print("[+] Response from Tor site:\n")
        print(response.decode())
        sock.close()
    except Exception as e:
        print("[-] Tor connection failed:", e)

if __name__ == "__main__":
    test_tor_connection()
