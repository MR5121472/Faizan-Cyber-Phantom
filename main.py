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
    print(f"\n🔥 Faizan™ Privacy Proxy System v{VERSION}")
    print("🔒 Secure. Stealth. Powerful.\n")

def main():
    intro()      # ← یہ نئی لائن added ہے
    banner()     # ← پرانا banner بھی برقرار رہے گا
    start_proxy()

if __name__ == "__main__":
    main()
