from core.proxy_engine import ProxyEngine
from config.settings import VERSION
import os
import time
from colorama import init, Fore, Style
from termcolor import colored
from core.proxy_engine import ProxyEngine

# Version info
VERSION = "3.0"

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clear_screen()
    print(Fore.RED + "="*70)
    print(Fore.RED + Style.BRIGHT + f"🔥 Faizan™ Privacy Proxy System v{VERSION}")
    print(Fore.YELLOW + "-"*70)
    print(Fore.CYAN + "🔐 Secure. Stealth. Powerful.")
    print(Fore.GREEN + "🛡️  Developed & Secured by:")
    print(Fore.MAGENTA + "👑  Muhammad Faizan Naeem")
    print(Fore.BLUE + "✍️  Known As: فیضانؔ مغل — The Cyber Phantom of Pakistan")
    print(Fore.RED + "="*70)
    time.sleep(2)

def banner():
    print()
    print(Fore.RED + Style.BRIGHT + "="*70)
    print(Fore.RED + Style.BRIGHT + f"🔥 Welcome to Faizan™ Privacy Proxy System v{VERSION}")
    print(Fore.YELLOW + "-"*70)
    print(Fore.CYAN + "🔒 Enabling ultra-secure encrypted proxy operations")
    print(Fore.GREEN + "🕵️ Running in stealth mode...")
    print(Fore.RED + "-"*70)
    print()

def main():
    intro()
    banner()

    proxy = ProxyEngine()  # Default 127.0.0.1:9050 (Tor)
    proxy.start_proxy()

    # Test connection to check.torproject.org on port 80
    if proxy.connect("check.torproject.org", 80):
        print(Fore.GREEN + "[+] Successfully connected to Tor proxy!")
        # Send HTTP GET request
        http_request = b"GET / HTTP/1.1\r\nHost: check.torproject.org\r\n\r\n"
        proxy.send_data(http_request)
        response = proxy.receive_data()
        if response:
            print(Fore.CYAN + "[+] Response preview:\n")
            # Print first 500 chars of response nicely
            print(response[:500].decode(errors='ignore'))
        proxy.close_connection()
    else:
        print(Fore.RED + "[-] Failed to connect via Tor proxy. Please ensure Tor is running on 127.0.0.1:9050")

if __name__ == "__main__":
    main()
