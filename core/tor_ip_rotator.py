import socket

def rotate_ip():
    try:
        tor_control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tor_control.connect(("127.0.0.1", 9051))  # Tor control port
        tor_control.send(b'AUTHENTICATE ""\r\n')  # No password
        response = tor_control.recv(1024)
        if b'250 OK' not in response:
            return False

        tor_control.send(b'SIGNAL NEWNYM\r\n')
        response = tor_control.recv(1024)
        tor_control.close()

        return b'250 OK' in response
    except Exception as e:
        print(f"[!] Tor IP rotation failed: {e}")
        return False
