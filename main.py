import os
import time
import socket
import subprocess
from stem.control import Controller

# ----------------------- INTERFACE ---------------------------
def banner():
    print("\033[95m" + "="*80)
    print("                      \U0001F525 FAIZAN™ PRIVACY PROXY SYSTEM v3.2")
    print("\033[94m" + "-"*80)
    print("\033[93m\U0001F512 ULTRA SECURE. STEALTH. POWERFUL.            \033[92m\U0001F6E1️  DEVELOPED BY:")
    print("\U0001F451  \033[1;96mMUHAMMAD FAIZAN NAEEM")
    print("✍️  AKA: \033[92mFAIZAN MUGHAL — THE CYBER PHANTOM OF PAKISTAN")
    print("\033[95m" + "="*80)
    print("="*80)
    print("                 \U0001F525 \033[93mWELCOME TO FAIZAN™ PRIVACY PROXY SYSTEM v3.2")
    print("\033[94m" + "-"*80)
    print("               \U0001F512 \033[93mENABLING ULTRA-SECURE ENCRYPTED PROXY OPERATIONS")
    print("                         \U0001F575️  \033[91mRUNNING IN STEALTH MODE...")
    print("\033[94m" + "-"*70 + "\033[0m")

# ----------------------- TOR STARTER ---------------------------
def start_tor():
    print("[*] Launching embedded Tor from script...")
    torrc_path = os.path.join(os.getcwd(), "torrc")
    try:
        tor_process = subprocess.Popen(
            ["tor", "-f", torrc_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(10)
        return tor_process
    except Exception as e:
        print(f"[x] Failed to start Tor: {e}")
        return None

# ----------------------- TOR IP ROTATION ------------------------
def rotate_ip():
    print("[*] Rotating IP via Tor network...")
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='mySecret123')
            controller.signal("NEWNYM")
            print("[✓] IP rotated successfully via Tor.")
    except Exception as e:
        print("[×] Tor IP rotation failed:", e)

# ------------------------ TEST TOR CONNECTION --------------------
def test_tor_connection():
    print("\n🌐 Testing Tor Proxy Connection via SOCKS5")
    import socks
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

    try:
        sock = socket.socket()
        sock.settimeout(10)
        sock.connect(("check.torproject.org", 80))
        sock.sendall(b"GET / HTTP/1.1\r\nHost: check.torproject.org\r\n\r\n")
        response = sock.recv(4096)
        print("[+] Response from Tor site:\n")
        print(response.decode())
        sock.close()
    except Exception as e:
        print("[-] Tor connection failed:", e)

# ------------------------ MAIN FUNCTION -------------------------
def main():
    banner()
    tor_process = start_tor()
    if not tor_process:
        print("[×] Could not start Tor. Exiting.")
        return

    time.sleep(5)
    rotate_ip()
    test_tor_connection()

    print("\n[*] All operations completed.")
    try:
        tor_process.terminate()
    except:
        pass

if __name__ == "__main__":
    main()
