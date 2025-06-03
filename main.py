from core.proxy_engine import ProxyEngine
from config.settings import VERSION

import os
import time
from core.proxy_engine import ProxyEngine
from config.settings import VERSION

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_border():
    print("=" * 80)

def intro():
    clear_screen()
    print_border()
    print(f"{'🔥 FAIZAN™ PRIVACY PROXY SYSTEM v' + VERSION:^80}")
    print("-" * 80)
    print("🔐 ULTRA SECURE. STEALTH. POWERFUL.".ljust(55) + "🛡️  DEVELOPED BY:")
    print("👑  MUHAMMAD FAIZAN NAEEM".ljust(55))
    print("✍️  AKA: FAIZAN MUGHAL — THE CYBER PHANTOM OF PAKISTAN".ljust(80))
    print_border()
    time.sleep(1)

def banner():
    print_border()
    print(f"{'🔥 WELCOME TO FAIZAN™ PRIVACY PROXY SYSTEM v' + VERSION:^80}")
    print("-" * 80)
    print("🔒 ENABLING ULTRA-SECURE ENCRYPTED PROXY OPERATIONS".center(80))
    print("🕵️ RUNNING IN STEALTH MODE...".center(80))
    print("-" * 80)

def main():
    intro()
    banner()

    proxy = ProxyEngine()
    try:
        proxy.start_proxy()
        if proxy.connect("check.torproject.org", 80):
            print("\n[+] CONNECTED SUCCESSFULLY VIA TOR PROXY!")
        else:
            print("\n[-] FAILED TO CONNECT. PLEASE ENSURE TOR IS RUNNING ON 127.0.0.1:9050")
    except Exception as e:
        print(f"\n[-] UNEXPECTED ERROR: {e}")

if __name__ == "__main__":
    main()
