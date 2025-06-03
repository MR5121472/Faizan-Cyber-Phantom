from core.proxy_engine import ProxyEngine
from config.settings import VERSION
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clear_screen()
    print("\n" + "="*70)
    print(f"🔥 Faizan™ Privacy Proxy System v{VERSION}")
    print("-"*70)
    print("🔐 Secure. Stealth. Powerful.")
    print("🛡️  Developed & Secured by:")
    print("👑  Muhammad Faizan Naeem")
    print("✍️  Known As: فیضانؔ مغل — The Cyber Phantom of Pakistan")
    print("="*70)
    time.sleep(2)

def banner():
    print("\n" + "-"*70)
    print(f"🔥 Welcome to Faizan™ Privacy Proxy System v{VERSION}")
    print("🔒 Enabling ultra-secure encrypted proxy operations")
    print("🕵️ Running in stealth mode...")
    print("-"*70 + "\n")
    time.sleep(1)

def main():
    intro()
    banner()
    proxy = ProxyEngine()
    proxy.start_proxy()
    # Example: connect to example.com port 80 (HTTP)
    if proxy.connect('example.com', 80):
        proxy.send_data(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        response = proxy.receive_data()
        print(response.decode(errors='ignore'))
        proxy.close_connection()

if __name__ == "__main__":
    main()
