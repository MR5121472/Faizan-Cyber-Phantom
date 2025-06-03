from core.proxy_engine import ProxyEngine
from config.settings import VERSION
import os
import time
from core.proxy_engine import ProxyEngine
from config.settings import VERSION

# ANSI COLOR CODES
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
    print(f"{YELLOW}{BOLD}{'🔥 FAIZAN™ PRIVACY PROXY SYSTEM v' + VERSION:^80}{RESET}")
    print(f"{CYAN}{'-' * 80}{RESET}")
    print(f"{GREEN}🔐 ULTRA SECURE. STEALTH. POWERFUL.".ljust(55) + f"{BLUE}🛡️  DEVELOPED BY:{RESET}")
    print(f"{GREEN}👑  MUHAMMAD FAIZAN NAEEM".ljust(55))
    print(f"{GREEN}✍️  AKA: FAIZAN MUGHAL — THE CYBER PHANTOM OF PAKISTAN".ljust(80))
    print_border()
    time.sleep(1)

def banner():
    print_border()
    print(f"{YELLOW}{BOLD}{'🔥 WELCOME TO FAIZAN™ PRIVACY PROXY SYSTEM v' + VERSION:^80}{RESET}")
    print(f"{CYAN}{'-' * 80}{RESET}")
    print(f"{RED}{BOLD}{'🔒 ENABLING ULTRA-SECURE ENCRYPTED PROXY OPERATIONS':^80}{RESET}")
    print(f"{RED}{'🕵️ RUNNING IN STEALTH MODE...':^80}{RESET}")
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
