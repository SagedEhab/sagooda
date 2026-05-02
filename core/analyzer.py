from core.banner import grab_banner

COMMON_SERVICES = {
    21: ("FTP", "Check anonymous login"),
    22: ("SSH", "Check weak credentials"),
    23: ("Telnet", "Insecure service"),
    25: ("SMTP", "Check for open relay"),
    53: ("DNS", "Check DNS config"),
    80: ("HTTP", "Test for XSS / SQLi"),
    110: ("POP3", "Check mail security"),
    139: ("NetBIOS", "Possible file sharing"),
    143: ("IMAP", "Check mail security"),
    443: ("HTTPS", "Check SSL/TLS config"),
    445: ("SMB", "Check SMB vulnerabilities"),
    3306: ("MySQL", "Check database exposure"),
    3389: ("RDP", "Remote desktop risk"),
    8080: ("HTTP-Alt", "Alternate web service"),
    8000: ("HTTP", "Development web server"),
}

def analyze_ports(ip, ports):
    analysis = []

    for port in ports:
        service = "Unknown"
        suggestion = "Needs investigation"
        banner = grab_banner(ip, port)

        if port in COMMON_SERVICES:
            service, suggestion = COMMON_SERVICES[port]

        if port >= 49152:
            service = "Ephemeral"
            suggestion = "Temporary system port"

        analysis.append((port, service, suggestion, banner))

    return analysis
