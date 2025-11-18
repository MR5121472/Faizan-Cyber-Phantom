import os
import time
import socket
import subprocess
import ssl
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
    
    # Global socket settings set karna
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket
    
    target_host = "check.torproject.org"
    target_port = 443
    
    # Sahi request string banaya gaya (Line 62 yahan shuru ho rahi hai)
    request = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {target_host}\r\n"
        f"Connection: close\r\n"
        f"User-Agent: FAIZAN_Phantom_V3.2\r\n"
        f"\r\n"
    )
    
    try:
        # Baaki code ki indentation theek hai
        sock = socket.socket()
        sock.settimeout(10)
        
        # 1. Tor proxy ke zariye 443 port tak connect hona
        sock.connect((target_host, target_port))
        
        # 2. Connection ko SSL/TLS se wrap karna (HTTPS ke liye zaroori)
        context = ssl.create_default_context()
        ssock = context.wrap_socket(sock, server_hostname=target_host)

        # 3. Data SIRF ssock ke zariye bhejna
        ssock.sendall(request.encode('utf-8'))
        
        response_bytes = b''
        while True:
            chunk = ssock.recv(4096)
            if not chunk:
                break
            response_bytes += chunk
            
        print("[+] Response from Tor site:\n")
        print(response_bytes.decode('utf-8', errors='ignore'))
        
        # 4. Sirf SSL socket ko band karna
        ssock.close() 
        
    except Exception as e:
        print(f"[-] Tor connection failed: {e}")

# ------------------------ MAIN FUNCTION -------------------------
def main_background():
    # 1. 'tor_process' ko start_tor() se hasil karein
    # (Yeh line banner() aur baki setup ke baad aayegi)
    tor_process = start_tor() 
    
    # Check karein agar Tor shuru nahi hua
    if not tor_process:
        print("[×] Could not start Tor. Exiting.")
        return 1

    # IP ko rotate karein (Initial Rotation)
    rotate_ip()

    print("\n[✓] Tor Proxy is now running on SOCKS5: 127.0.0.1:9050")
    print("[!] You can now use 'curl' and other tools in this terminal.")
    
    # 2. Ab PID ko print karein, kyunki tor_process available hai
    print(f"[*] Tor Process ID (PID): {tor_process.pid}") 
    return tor_process

# ------------------------ MAIN FUNCTION (UPDATED) -------------------------
if __name__ == "__main__":
    # main_background() ko call karein. Ab yeh ya to process object return karega ya 1.
    process = main_background()
    
    # Script ko chalte rehne dein
    if process != 1:
        try:
            while True:
                # Automatic IP rotation every 10 seconds
                time.sleep(10)
                rotate_ip()
                
        except KeyboardInterrupt:
            print("\n[!] Shutting down Tor process...")
            process.terminate()
            print("[✓] Faizan-Cyber-Phantom shut down successfully.")
