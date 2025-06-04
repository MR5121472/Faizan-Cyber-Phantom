import os, time, socket, subprocess

# Colorful startup interface
def banner():
    print("\033[95m" + "="*80)
    print("                      \U0001F525 FAIZAN™ PRIVACY PROXY SYSTEM v3.2            ")
    print("\033[94m" + "-"*80)
    print("\033[93m\U0001F512 ULTRA SECURE. STEALTH. POWERFUL.            \033[92m\U0001F6E1️  DEVELOPED BY:")
    print("\U0001F451  \033[1;96mMUHAMMAD FAIZAN NAEEM")
    print("\u270D\uFE0F  AKA: \033[92mFAIZAN MUGHAL — THE CYBER PHANTOM OF PAKISTAN")
    print("\033[95m" + "="*80)
    print("="*80)
    print("                 \U0001F525 \033[93mWELCOME TO FAIZAN™ PRIVACY PROXY SYSTEM v3.2      ")
    print("\033[94m" + "-"*80)
    print("               \U0001F512 \033[93mENABLING ULTRA-SECURE ENCRYPTED PROXY OPERATIONS    ")
    print("                         \U0001F575️  \033[91mRUNNING IN STEALTH MODE...                 ")
    print("\033[94m" + "-"*70 + "\033[0m")

# Start Tor process

def start_tor():
    print("[*] Launching embedded Tor from script...")
    torrc_path = os.path.join(os.getcwd(), "torrc")
    try:
        tor_process = subprocess.Popen(
            ["tor", "-f", torrc_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(10)  # wait to bootstrap
        return tor_process
    except Exception as e:
        print(f"[×] Failed to start Tor: {e}")
        return None

# Signal NEWNYM

def rotate_ip():
    print("[*] Rotating IP via Tor network...")
    try:
        with socket.create_connection(("127.0.0.1", 9051), timeout=5) as s:
            s.sendall(b'AUTHENTICATE ""\r\n')
            if b'250' not in s.recv(1024):
                raise Exception("AUTH failed")
            s.sendall(b'SIGNAL NEWNYM\r\n')
            if b'250' in s.recv(1024):
                print("[✔] Tor IP rotation signal sent successfully.\n")
            else:
                print("[×] Tor did not accept NEWNYM signal.")
    except Exception as e:
        print(f"[!] Tor IP rotation failed: {e}")
        print("[-] FAILED TO CONNECT. PLEASE CHECK TOR OR PROXY SETTINGS.\n")

# Main Execution

def main():
    banner()
    tor_proc = start_tor()
    if not tor_proc:
        return

    try:
        while True:
            rotate_ip()
            time.sleep(12)  # every 12 seconds
    except KeyboardInterrupt:
        print("\n[✓] User interrupted. Cleaning up...")
    finally:
        if tor_proc:
            tor_proc.terminate()
            print("[✓] Tor process terminated. System restored.\n")

if __name__ == "__main__":
    main()
