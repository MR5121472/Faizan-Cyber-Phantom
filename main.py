#!/usr/bin/env python3
import os, time, socket, subprocess

def intro():
    # Stylish intro
    print("\033[95m" + "="*80)
    print("                      🔥 FAIZAN™ PRIVACY PROXY SYSTEM v3.1            ")
    print("\033[94m" + "-"*80)
    print("\033[93m🔐 ULTRA SECURE. STEALTH. POWERFUL.            \033[92m🛡️  DEVELOPED BY:")
    print("👑  \033[1;96mMUHAMMAD FAIZAN NAEEM")
    print("✍️  AKA: \033[92mFAIZAN MUGHAL — THE CYBER PHANTOM OF PAKISTAN")
    print("\033[95m" + "="*80)
    print("="*80)
    print("                 🔥 \033[93mWELCOME TO FAIZAN™ PRIVACY PROXY SYSTEM v3.1      ")
    print("\033[94m" + "-"*80)
    print("               🔒 \033[93mENABLING ULTRA-SECURE ENCRYPTED PROXY OPERATIONS    ")
    print("                         🕵️  \033[91mRUNNING IN STEALTH MODE...                 ")
    print("\033[94m" + "-"*70 + "\033[0m\n")

    # Lite Mode IP Simulation
    print("[+] Initializing Faizan™ Privacy Proxy Engine...")
    print("[+] Proxy Engine started in Lite Mode (No external libs)")
    print("[*] Starting IP rotation simulation every 2 seconds...\n")

    fake_ips = ["192.168.44.1", "218.212.99.93", "161.243.15.218", "24.26.97.83"]
    for ip in fake_ips:
        print(f"[✔] IP changed to: {ip}")
        time.sleep(0.5)

    print("\n[✓] IP rotation simulation complete.\n")

def start_tor():
    print("[*] Launching embedded Tor from script...")
    torrc_path = os.path.join(os.getcwd(), "torrc")
    try:
        tor_process = subprocess.Popen(
            ["tor", "-f", torrc_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(7)  # Wait for Tor to bootstrap
        return tor_process
    except Exception as e:
        print(f"[×] Failed to start Tor: {e}")
        return None

def send_signal_newnym():
    print("[*] Rotating IP via Tor network...")
    try:
        with socket.create_connection(("127.0.0.1", 9051), timeout=5) as s:
            s.sendall(b'AUTHENTICATE ""\r\n')
            response = s.recv(1024)
            if b'250 OK' not in response:
                raise Exception("AUTH failed")

            s.sendall(b'SIGNAL NEWNYM\r\n')
            resp = s.recv(1024)
            if b'250 OK' in resp:
                print("[✔] Tor IP rotation signal sent successfully.\n")
            else:
                print("[×] Tor did not accept NEWNYM signal.")
    except Exception as e:
        print(f"[!] Tor IP rotation failed: {e}")
        print("[-] FAILED TO CONNECT. PLEASE CHECK TOR OR PROXY SETTINGS.\n")

def main():
    intro()
    tor_proc = start_tor()
    send_signal_newnym()

    # Auto cleanup (optional)
    if tor_proc:
        tor_proc.terminate()
        print("[✓] Tor process terminated. System restored.\n")

if __name__ == "__main__":
    main()
