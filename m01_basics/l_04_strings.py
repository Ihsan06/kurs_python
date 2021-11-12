from pprint import pprint

device1_str = " r3-L-n7, cisco, catalyst 2968, ios "

# Split
print("STRING STRIP, SPLIT, REPLACE")
device1 = device1_str.split(",")
print("device1 using split:")
print("    ", device1)

# Strip get gid off blanks at the beginning and end
device1 = device1_str.strip().split(",")
print("device1 using strip and split:")
print("    ", device1)

# Remove Blanks, change all the blanks into nothing mit replace, but look catalyst
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split:\n    ", device1)

# Remove Blanks, change Comme to Colon --> keine Liste mehr
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print("device1 replaced blanks, comma to colon:")
print("   ", device1_str_colon)

# Loop with Strip and Split
device1 = list()
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and strip for each item:")
print("   ", device1)

# Strip and Split, single line using Comprehension
device1 = [item.strip() for item in device1_str.split(",")]
print("device1 using list comprehension")
print("   ", device1)

# Ignoring Case
print("\n\nIgnoring Case")
model = "CSR1000V"
if model == "csr1000v":
    print(f'matched: {model}')
else:
    print(f"didn't match: {model}")

model = "CSR1000V"
if model.lower() == "csR1000v".lower():
    print(f"matched with lower(): {model}")
else:
    print(f"didn't match: {model}")

# Finding Substring
print("\n\nFinding Substring")
version = "Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.11.1a, Release Software (fc1) "
expected_version = "Version 16.11.1a"
index = version.find(expected_version)
if index >= 0:
    print(f"found version: {expected_version} \nat location: {index} ")
else:
    print(f"not found: {expected_version}")

# Separating String Components
print("\n\nSeparating Version String Components")
version_info = version.split(",")
for part_no, version_info_part in enumerate(version_info):
    print(f"version part {part_no}: {version_info_part.strip()}")

show_interface_stats = """
GigabitEthernet1
            Switching path  Pkts In     Chars In    Pkts Out     Chars Out    
                 Processor    25376      1529598        8242        494554
               Route cache        0            0           0             0
         Distributed cache   496298     68647894    68647894    6864789443  
                     Total   521674     62177492    68647894    6864789443

GigabitEthernet2
            Switching path  Pkts In     Chars In    Pkts Out     Chars Out    
                 Processor    25376      1529598           0             0
               Route cache        0            0           0             0
         Distributed cache   496298     68647894           0             0  
                     Total   521674     62177492           0             0

GigabitEthernet3 is disabled

Loopback21
            Switching path  Pkts In     Chars In    Pkts Out     Chars Out    
                 Processor        0            0           0             0
               Route cache        0            0           0             0
         Distributed cache        0            0           0             0  
                     Total        0            0           0             0

Loopback55
            Switching path  Pkts In     Chars In    Pkts Out     Chars Out    
                 Processor        0            0           0           241
               Route cache        0            0           0             0
         Distributed cache        0            0           0             0  
                     Total        0            0           0           241

Loopback100
            Switching path  Pkts In     Chars In    Pkts Out     Chars Out    
                 Processor        0            0          43          2886
               Route cache        0            0           0             0
         Distributed cache        0            0           0             0  
                     Total        0            0          43          2886
"""
print(show_interface_stats)

interface_counters = dict()
show_interface_stats_lines = show_interface_stats.splitlines()
for index, stats_line in enumerate(show_interface_stats_lines):
    if stats_line.find('GigabitEthernet', 0) == 0:

        totals_line = show_interface_stats_lines[index + 5]
        interface_counters[stats_line] = totals_line.split()[1:]

print("\n\n---------Interface Counters ---------")
pprint(interface_counters)

show_arp = """
Protocol    Address          Age (min)    Hardware Addr     Type    Interface
Internet    10.10.28.48              -    8858.56bb.e99c    ARPA    GigabitEthernet1
Internet    10.10.28.288            14    8858.56bb.8be2    ARPA    GigabitEthernet2
Internet    10.10.28.254             8    8858.ad9e.444c    ARPA    GigabitEthernet3
"""
print(show_arp)

arp_table = dict()
for arp_line in show_arp.splitlines():
    if arp_line.lower().find("internet", 0) == 0:
        arp_table[arp_line[10:24].strip()] = arp_line[42:56]

print("\n\n------ ARP Table--------------")
pprint(arp_table)
