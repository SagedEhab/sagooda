#!/usr/bin/env python3

import argparse
import ipaddress
from core.scanner import scan_ports
from core.analyzer import analyze_ports
from utils.formatter import print_report


def scan_target(ip):
    print(f"\n[*] Scanning {ip}...")
    open_ports = scan_ports(str(ip))

    print(f"DEBUG: Open ports → {open_ports}")

    if open_ports:
        analysis = analyze_ports(str(ip), open_ports)
        print_report(str(ip), analysis)


def main():
    parser = argparse.ArgumentParser(description="Sagooda Smart Recon Tool")
    parser.add_argument("-t", "--target", required=True, help="Target IP or subnet")

    args = parser.parse_args()
    target = args.target

    try:
        if "/" in target:
            network = ipaddress.ip_network(target, strict=False)
            for ip in network.hosts():
                scan_target(ip)
        else:
            scan_target(target)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
