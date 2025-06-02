from core.proxy_engine import start_proxy
from config.settings import VERSION

def banner():
    print(f"\n🔥 Faizan™ Privacy Proxy System v{VERSION}")
    print("🔒 Secure. Stealth. Powerful.\n")

def main():
    banner()
    start_proxy()

if __name__ == "__main__":
    main()
