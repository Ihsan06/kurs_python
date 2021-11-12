from random import choice
import string
from pprint import pprint
from operator import itemgetter
from tabulate import tabulate

devices = list()        # Create Empty List for holding Devices

# For Loop to create larger number of Devices

for index in range(1, 11):

    # Create Device Dictionary
    device = dict()

    # Random Device Name
    device["name"] = (
        choice(["r2", "r3", "r4", "r6", "r18"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )

    # Random vendor
# from choice of cisco, juniper, arista
    device["vendor"] = choice(["cisco", "juniper", "arista"])
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04", "14.87X", "8.12(S).018", "28.45"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.345"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])

    device["ip"] = "10.0.0." + str(index)

    # Nicely formatted print of this one device
    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")

    # Add this device to the list of devices

    devices.append(device)

# Use PPrint to print Data As-Is
print("\n_____Devs as List of Dicts")
pprint(devices)

# Use Tabulate to print table of devices
print("\n------ sorted devices in tabular format --------")

# print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))
sorted_devices = sorted(devices, key=itemgetter("vendor", "os", "version"))
print(tabulate(sorted_devices, headers="keys"))
