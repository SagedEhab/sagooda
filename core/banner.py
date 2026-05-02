import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)

        s.connect((ip, port))

        # Send simple HTTP request
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")

        banner = s.recv(1024)
        s.close()

        return banner.decode(errors="ignore").strip()

    except:
        return None
