from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

def process_packet(packet):
    time_stamp = datetime.now().strftime("%H:%M:%S")

    if IP in packet:
        ip = packet[IP]
        src = ip.src
        dst = ip.dst
        proto = ip.proto
        proto_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(proto, str(proto))

        print(f"\n[{time_stamp}] Protocol: {proto_name}")
        print(f"  From {src} → To {dst}")

        if proto == 6 and TCP in packet:
            tcp = packet[TCP]
            print(f"  TCP Port: {tcp.sport} → {tcp.dport}")
            if tcp.payload:
                print(f"  Payload (first 50 bytes): {bytes(tcp.payload)[:50]}")

        elif proto == 17 and UDP in packet:
            udp = packet[UDP]
            print(f"  UDP Port: {udp.sport} → {udp.dport}")
            if udp.payload:
                print(f"  Payload (first 50 bytes): {bytes(udp.payload)[:50]}")

        elif proto == 1 and ICMP in packet:
            icmp = packet[ICMP]
            print(f"  ICMP Type: {icmp.type}, Code: {icmp.code}")

        print("-" * 60)

print("📡 Sniffing started... Press Ctrl+C to stop.")
sniff(filter="ip", prn=process_packet, store=False)