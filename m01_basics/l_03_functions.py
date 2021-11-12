from random import choice
import string
from tabulate import tabulate


def create_devices(num_devices=1, num_subnets=1):

    # Create list of devices
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets requested")
        return created_devices

    for subnet_index in range(1, num_subnets+1):

        for device_index in range(1, num_devices+1):

            # Create Device Dictionary
            device = dict()

            # Random device name

            device["name"] = (
                    choice(["r2", "r3", "r4", "r6", "r18"])
                    + choice(["L", "U"])
                    + choice(string.ascii_letters)
            )
            # Random vendor from choice of cisco, juniper, arista
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

            device["ip"] = "10.0." + str(subnet_index) + "." + str(device_index)

            created_devices.append(device)

    return created_devices


# -------- Main programm -----------
if __name__ == '__main__':

    devices = create_devices(num_devices=4, num_subnets=5)
    print("\n", tabulate(devices, headers="keys"))
