import time
from stem import Signal
from stem.control import Controller
import requests

def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()  # Default password-less or set your password here
        controller.signal(Signal.NEWNYM)
        print("[+] Tor NEWNYM signal sent: IP should change now.")

def get_current_ip():
    try:
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        response = requests.get("http://check.torproject.org/api/ip", proxies=proxies, timeout=10)
        ip = response.json().get("IP")
        print(f"[+] Current Tor IP: {ip}")
        return ip
    except Exception as e:
        print(f"[-] Could not get IP: {e}")
        return None

def auto_ip_rotation(interval=2):
    print("[*] Starting Auto IP Rotation every", interval, "seconds.")
    current_ip = None
    while True:
        renew_tor_ip()
        time.sleep(5)  # Tor needs some seconds to switch IP
        new_ip = get_current_ip()
        if new_ip != current_ip:
            print(f"[+] IP Changed to: {new_ip}")
            current_ip = new_ip
        else:
            print("[-] IP did not change, retrying...")
        time.sleep(interval)

def start_proxy():
    print("[+] Initializing Faizan™ Privacy Proxy Engine...")
    auto_ip_rotation()
