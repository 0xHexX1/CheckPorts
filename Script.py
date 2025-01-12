import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """Check if a specific port is open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # 1-second timeout
            s.connect((ip, port))
            return port, True
    except:
        return port, False

def main():
    print("=== Basic Port Scanner ===")
    target = input("Enter target IP or domain: ")

    # Common ports to scan
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389]
    print(f"\nScanning {len(common_ports)} common ports on {target}...\n")

    open_ports = []

    # Multithreading for faster scanning
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda port: scan_port(target, port), common_ports)
        for port, is_open in results:
            if is_open:
                open_ports.append(port)
                print(f"[+] Port {port} is open.")

    if open_ports:
        print("\nOpen ports detected:")
        for port in open_ports:
            print(f" - {port}")
    else:
        print("\nNo open ports found.")

    print("\nScan complete.")

if __name__ == "__main__":
    main()
