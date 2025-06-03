
import os
import time
from core.proxy_engine import start_proxy
from config.settings import VERSION

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
    start_proxy()

if __name__ == "__main__":
    main()
