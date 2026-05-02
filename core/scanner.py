import socket
from concurrent.futures import ThreadPoolExecutor

def scan_single_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)

    result = s.connect_ex((ip, port))
    s.close()

    if result == 0:
        return port
    return None


def scan_ports(ip):
    open_ports = []

    ports = range(1, 65536)  # ALL ports

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_single_port(ip, p), ports)

    for r in results:
        if r:
            open_ports.append(r)

    return open_ports

