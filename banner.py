import socket

def banner_grab(ip, port):
    try:
        # Create a socket connection
        s = socket.socket()
        s.settimeout(5)  # Timeout after 5 seconds

        print(f"[+] Connecting to {ip}:{port}")
        s.connect((ip, port))
        
        # Send a dummy message (for HTTP, can also be b'HEAD / HTTP/1.0\r\n\r\n')
        s.send(b'Hello\r\n')
        
        # Receive the banner
        banner = s.recv(1024)
        print(f"[+] Banner from {ip}:{port}:\n{banner.decode().strip()}")
        s.close()

    except socket.timeout:
        print(f"[-] Timeout while connecting to {ip}:{port}")
    except socket.error as e:
        print(f"[-] Could not connect to {ip}:{port}: {e}")

# Example usage
target_ip = input("Enter target IP: ")
target_ports = [21, 22, 25, 80, 443, 8080]

for port in target_ports:
    banner_grab(target_ip, port)

