def print_report(ip, analysis):
    print(f"\n=== Sagooda Smart Report for {ip} ===\n")

    for port, service, suggestion, banner in analysis:
        print(f"[+] Port {port} ({service})")
        print(f"   → {suggestion}")

        if banner:
            print(f"   → Banner: {banner[:100]}")
