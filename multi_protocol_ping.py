#!/usr/bin/env python3

from scapy.all import *  # Import all necessary Scapy modules

def icmp_ping(destination):
    """
    Send ICMP echo requests (ping) to the target destination.

    Args:
        destination (str): Target IP or IP range.

    Returns:
        ans: Answered packets.
    """
    # ICMP ping scan
    ans, unans = sr(IP(dst=destination)/ICMP())
    return ans

def tcp_ping(destination, dport):
    """
    Send a TCP SYN packet to check if a host responds (TCP ping).

    Args:
        destination (str): Target IP address.
        dport (int): TCP port to send SYN to.

    Returns:
        ans: Answered packets.
    """
    # TCP SYN scan for responsiveness
    ans, unans = sr(IP(dst=destination)/TCP(dport=dport, flags="S"))
    return ans

def udp_ping(destination):
    """
    Send a UDP packet to check if host responds (less reliable ping).

    Args:
        destination (str): Target IP or IP range.

    Returns:
        ans: Answered packets.
    """
    # UDP packet to port 0 to elicit ICMP response if host is alive
    ans, unans = sr(IP(dst=destination)/UDP(dport=0))
    return ans

def answer_summary(ans):
    """
    Print a summary of responses from hosts that replied.

    Args:
        ans: List of (sent, received) packet tuples.
    """
    for send, recv in ans:
        print(recv.sprintf("%IP.src% is alive"))

def main():
    """
    Run ICMP, TCP, and UDP ping scans and summarize live hosts.
    """
    print("** ICMP Ping **")
    ans = icmp_ping("192.168.255.1")
    answer_summary(ans)

    print("** TCP Ping ***")
    ans = tcp_ping("192.168.255.1", 22)
    answer_summary(ans)

    print("** UDP Ping ***")
    ans = udp_ping("192.168.255.1")
    answer_summary(ans)

# Entry point check
if __name__ == "__main__":
    main()
