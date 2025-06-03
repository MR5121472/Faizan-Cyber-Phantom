import os
import time
from core.proxy_engine import ProxyEngine
from config.settings import VERSION

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_border():
    print(f"{CYAN}{'=' * 80}{RESET}")

def intro():
    clear_screen()
    print_border()
    print(f"{YELLOW}{BOLD}{'\ud83d\udd25 FAIZAN\u2122 PRIVACY PROXY SYSTEM v' + VERSION:^80}{RESET}")
    print(f"{CYAN}{'-' * 80}{RESET}")
    print(f"{GREEN}\ud83d\udd10 ULTRA SECURE. STEALTH. POWERFUL.".ljust(55) + f"{BLUE}\ud83d\udee1\ufe0f  DEVELOPED BY:{RESET}")
    print(f"{GREEN}\ud83d\udc51  MUHAMMAD FAIZAN NAEEM".ljust(55))
    print(f"{GREEN}\u270d\ufe0f  AKA: FAIZAN MUGHAL \u2014 THE CYBER PHANTOM OF PAKISTAN".ljust(80))
    print_border()
    time.sleep(1)

def banner():
    print_border()
    print(f"{YELLOW}{BOLD}{'\ud83d\udd25 WELCOME TO FAIZAN\u2122 PRIVACY PROXY SYSTEM v' + VERSION:^80}{RESET}")
    print(f"{CYAN}{'-' * 80}{RESET}")
    print(f"{RED}{BOLD}{'\ud83d\udd12 ENABLING ULTRA-SECURE ENCRYPTED PROXY OPERATIONS':^80}{RESET}")
    print(f"{RED}{'\ud83d\udd75\ufe0f RUNNING IN STEALTH MODE...':^80}{RESET}")
    print(f"{CYAN}{'-' * 80}{RESET}")

def main():
    intro()
    banner()

    proxy = ProxyEngine()
    try:
        proxy.start_proxy()
        if proxy.connect("check.torproject.org", 80):
            print(f"\n{GREEN}[+] CONNECTED SUCCESSFULLY VIA TOR PROXY!{RESET}")
        else:
            print(f"\n{RED}[-] FAILED TO CONNECT. PLEASE ENSURE TOR IS RUNNING ON 127.0.0.1:9050{RESET}")
    except Exception as e:
        print(f"\n{RED}[-] UNEXPECTED ERROR: {e}{RESET}")

if __name__ == "__main__":
    main()
    
