#!/usr/bin/env python3

from scapy.all import *  # Import all Scapy functionalities
import sys  # For command-line argument handling

def tcp_scan(destination, dport):
    """
    Perform a TCP SYN scan on the specified destination and port.

    Args:
        destination (str): Target IP address or hostname.
        dport (int): Destination TCP port to scan.

    Returns:
        str: Scan result indicating whether the port is open or not.
    """
    # Send a TCP SYN packet and wait for a response
    ans, unans = sr(IP(dst=destination)/TCP(sport=666, dport=dport, flags="S"))

    # Analyze responses
    for sending, returned in ans:
        # 'SA' indicates SYN-ACK, meaning the port is open
        if 'SA' in str(returned[TCP].flags):
            return destination + " port " + str(sending[TCP].dport) + " is open."
        else:
            return destination + " port " + str(sending[TCP].dport) + " is not open."

def main():
    """
    Entry point for command-line usage.
    Usage: script.py <destination> <port>
    """
    destination = sys.argv[1]  # Get target IP/host from command-line
    port = int(sys.argv[2])  # Get target port from command-line
    scan_result = tcp_scan(destination, port)  # Run scan
    print(scan_result)  # Output result

if __name__ == "__main__":
    main()  # Start program
