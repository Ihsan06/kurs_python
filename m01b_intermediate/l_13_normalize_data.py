from ipaddress import IPv4Address

print("\nNormalization tests\n")

device_1 = {
    "name": "sbx-n9kv-AO",
    "vendor": "cisco",
    "model": "Nexus9000 C9306v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
    1: "any data goes here",
}
device_2 = {
    "name": "SBX-n9kv-AO",
    "vendor": "Cisco",
    "model": "Nexus9000 C9306v Chassis",
    "os": "NXOS",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
    1: "any data goes here",
}
if (
    device_1["name"].lower() == device_2["name"].lower()
    and device_1["vendor"].lower() == device_2["vendor"].lower()
    and device_1["model"].lower() == device_2["model"].lower()
    and device_1["os"].lower() == device_2["os"].lower()
):
    print("--String lower() normalization works")
else:
    print("--String lower() normalization failed")

if (
    device_1["name"].casefold() == device_2["name"].casefold()
    and device_1["vendor"].casefold() == device_2["vendor"].casefold()
    and device_1["model"].casefold() == device_2["model"].casefold()
    and device_1["os"].casefold() == device_2["os"].casefold()
):
    print("--String Casefold() normalization works")
else:
    print("--String casefold() normalization failed")

# ------ MAC Address Normalization -----------

mac_adr_colons = "a0:b1:c2:d3:e4:f5"
mac_adr_caps = "A0:B1:C2:D3:e4:F5"
mac_adr_dots = "a0b1.c2d3.e4f5"
mac_adr_hyphens = "A0-B1-C2-D3-E4-F5"
mac_adr_wacky = "A0-b1.c2:D3.e4-f5"

mac_adr_norm = "a0b1c2d3e4f5"


# Return normalized MAC addresses
def normalize(mac):
    return mac.lower().replace(":", "").replace(".", "").replace("-", "")


if (
    normalize(mac_adr_colons)
    == normalize(mac_adr_caps)
    == normalize(mac_adr_dots)
    == normalize(mac_adr_hyphens)
    == normalize(mac_adr_wacky)
    == mac_adr_norm
):
    print("--MAC address normalization works")
else:
    print("--MAC address normalization failed")

# ------ IP Address normalization --------------

ip_addr_1 = "10.0.1.1"
ip_addr_2 = "10.000.001.001"
ip_addr_3 = "010.00.01.001"

if IPv4Address(ip_addr_1) == IPv4Address(ip_addr_2) == IPv4Address(ip_addr_3):
    print("--IP address normalization")
else:
    print("--IP address normalization failed")

# Funktioniert nicht
# ----- Device Data Normalization --------
# (see Napalm example)
