import os
import time
import socket
import subprocess
import ssl
from stem.control import Controller

# ----------------------- INTERFACE (BANNER) ---------------------------
def banner():
    print("\033[95m" + "="*80)
    print("                      \U0001F525 FAIZAN™ PRIVACY PROXY SYSTEM v3.2")
    print("\033[94m" + "-"*80)
    print("\033[93m\U0001F512 ULTRA SECURE. STEALTH. POWERFUL.            \033[92m\U0001F6E1️  DEVELOPED BY:")
    print("\U0001F451  \033[1;96mMUHAMMAD FAIZAN NAEEM")
    print("✍️ C9: \033[92mFAIZAN MUGHAL — THE CYBER PHANTOM OF PAKISTAN")
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
        time.sleep(10) # Tor ko initialize hone ka time dena
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
    print("\n🌐 Testing Tor Proxy Connection via SOCKS5...")
    try:
        import socks
    except ImportError:
        print("[-] PySocks is missing! Run: pip install PySocks")
        return

    # Global socket settings set karna
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket
    
    target_host = "check.torproject.org"
    target_port = 443
    
    request = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {target_host}\r\n"
        f"Connection: close\r\n"
        f"User-Agent: FAIZAN_Phantom_V3.2\r\n"
        f"\r\n"
    )
    
    try:
        sock = socket.socket()
        sock.settimeout(10)
        sock.connect((target_host, target_port))
        
        context = ssl.create_default_context()
        ssock = context.wrap_socket(sock, server_hostname=target_host)

        ssock.sendall(request.encode('utf-8'))
        
        response_bytes = b''
        while True:
            chunk = ssock.recv(4096)
            if not chunk:
                break
            response_bytes += chunk
            
        print("[+] Connection Successful! Response received from Tor.")
        # Agar poori HTML response nahi dekhni toh niche wali line ko comment (#) kar sakte hain
        # print(response_bytes.decode('utf-8', errors='ignore')[:500]) 
        ssock.close() 
        
    except Exception as e:
        print(f"[-] Tor connection failed: {e}")

# ------------------------ MAIN BACKGROUND FUNCTION -------------------------
def main_background():
    tor_process = start_tor() 
    
    if not tor_process:
        print("[×] Could not start Tor. Exiting.")
        return 1

    rotate_ip()

    print("\n[✓] Tor Proxy is now running on SOCKS5: 127.0.0.1:9050")
    print("[!] You can now use 'curl' and other tools in this terminal.")
    print(f"[*] Tor Process ID (PID): {tor_process.pid}") 
    return tor_process

# ------------------------ EXECUTION FLOW -------------------------
if __name__ == "__main__":
    # 1. Sabse pehle banner display hoga
    os.system('clear') # Screen clear karne ke liye takay banner top par aaye
    banner()
    
    # 2. Tor process background mein start hoga
    process = main_background()
    
    if process != 1:
        # 3. Proxy test run karein
        test_tor_connection()
        
        try:
            print("\n[*] Stealth mode active. Press CTRL+C to exit.")
            while True:
                # Automatic IP rotation every 10 seconds
                time.sleep(10)
                rotate_ip()
                
        except KeyboardInterrupt:
            print("\n[!] Shutting down Tor process...")
            process.terminate()
            print("[✓] Faizan-Cyber-Phantom shut down successfully.")
        
