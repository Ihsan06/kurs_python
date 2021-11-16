import scapy.all as scapy
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, ICMP, TCP

# Capture everything and print packet summaries
print("\n---- Packet summaries ---------")
capture = scapy.sniff(iface="ens33", count=10)
print(capture.nsummary())

# Capture dns and print packets
print("\n----- DNS packet summaries (collect 10 DNS packets) ------------")
capture = scapy.sniff(iface="ens33", filter="udp port 53", count=10)
print(capture.nsummary())

# Capture only DNS and print complete packets
print("\n\n----- DNS packets, complete (collect 10 DNS packets) ---------")
capture = scapy.sniff(iface="ens33", filter="udp port 53", count=10)
for packet in capture:
    print(packet.show())


# Capture and handle packets as they arrive
print("\n\n------- Capture and print packets as sniffed -----------------")


def print_packet(pkt):
    print("    ", pkt.summary())


scapy.sniff(iface="ens33", prn=print_packet, filter="tcp port https", count=10, timeout=10)


# Capture and handle packets as they arrive using lambda
print("\n\n----- Discovery hosts on network using manual ARP ping -------")
scapy.sniff(iface="ens33", prn=lambda pkt: print(f"    {pkt.summary()}"), filter="tcp port https", count=10, timeout=10)

# Discovery hosts on network using manual ARP PING
print("\n\n---- Discovery hosts on network using manual ARP PING--------")
ans, unans = scapy.srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.40.0/24"), timeout=2)

# Discovery hosts n network using ARPING function
print("----- Discovery hosts on network using ARPING function ------------")
ans, unans = scapy.arping("192.168.40.0/24")
ans.summary()

for res in ans.res:
    print(f"--> IP address discovered: {res[0].payload.pdst}")

# Discover hosts on networking using ICMP PING
# print("------ Discover hosts on networking using ICMP PING ---------------")
# ans, unans = scapy.sr(IP(dst="192.168.40.1-254")/ICMP(), timeout=1)
# ans.summary()

# TCP port scan
print("\n\n----- See what ports are open on a device --------------------")
while True:

    ip = input("IP address on which to scan port: ")
    if not ip:
        print("\n----- Ending port scanning")
        break

    # answers, unans = scapy.sr(IP(dst="192.168.40.254")/TCP(flags="S", sport=666, dport=[22, 80, 21, 443]), timeout=1)
    answers, unans = scapy.sr(IP(dst=ip)/TCP(flags="S", sport=666, dport=(1, 1024)), timeput=10)
    for answered in answers:
        print(f"---> open port: {answered[0].summary()}")

    print()
    for un_answered in unans:
        print(f"---> closed port. {un_answered[0].summary()}")

    print(f"\n----- Open/Closed port totals --------------")
    print(f"\tOpen ports: {len(answers)}")
    print(f"\tClosed ports: {len(unans)}")
