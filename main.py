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

from encryption.encryptor import generate_key, get_cipher, encrypt_data, decrypt_data

# Step 1: Key generate کریں
key = generate_key()

# Step 2: Cipher object بنائیں
cipher = get_cipher(key)

# Step 3: Encrypt کرنے کے لیے کوئی text دیں
data = "Faizan™ Proxy Test"

# Step 4: Encrypt کریں
encrypted = encrypt_data(cipher, data)

# Step 5: Decrypt کریں
decrypted = decrypt_data(cipher, encrypted)

# Step 6: Output پر result دیکھیں
print("🔐 Encrypted:", encrypted)
print("🔓 Decrypted:", decrypted)
