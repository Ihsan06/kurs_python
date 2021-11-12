from pprint import pprint
from random import choice
import copy
from util.create_utils import create_network

device = {
    "name": "r3-L-n7",
    "vendor": "cisco",
    "model": "catalyst 2968",
    "os": "ios",
    "interfaces": []
}

print("\n\n----- device with no interfaces ---------")
for key, value in device.items():
    print(F"{key:>16} : {value}")

interfaces = list()
for index in range(0, 8):
    interface = {
        "name": "g/0/0/" + str(index),
        "speed": choice(["10", "100", "1000"])
    }
    interfaces.append(interface)

device["interfaces"] = interface

print("\n\n----- device with interfaces ------------")
for key, value in device.items():
    if key != "interfaces":
        print(f"{key:>16} : {value}")
    else:
        print(f"{key:>16} :")
        for interface in interfaces:
            print(f"\t\t\t\t\t{interface}")
print()
print("\n\n------ device with interfaces using pprint-------")
pprint(device)

print("\n\n----- network with devices and interfaces")
network = create_network(num_devices=4, num_subnets=4)
pprint(network)

print("\n\n----- information about network --------------")
print(f"-- number of subnets: {len(network['subnets'])}")
print(f"-- list of subnets:     {network['subnets'].keys()}")
print(F"-- list of subnets w/o extraneous: {', '.join(network['subnets'])}")

print("\n------- network and devices nicely formatted ---------")
for subnet_address, subnet in network["subnets"].items():
    print(f"\n-- subnet_ {subnet_address}")
    for device in subnet["devices"]:
        print(f"    I-- device: {device['name']:8}  {device['ip']:18}    {device['vendor']:>18}  : {device['os']}")

print("\n\n----- remember assignment vs shallow copy vs deep copy ----------")
print("       modify 'network only, and see if assign/copy/deepcopy versions reflect that change")
network_assign = network
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "different name assigned"
print(f"   --- network == network_assign :   {network!=network_assign}")

network_copy = copy.copy(network)
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "another different name, copy this time"
print(f"   --- network == network_copy :   {network!=network_copy}")

network_deepcopy = copy.deepcopy(network)
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "this is with deepcopy"
print(f"   --- network == network_deepcopy :   {network!=network_deepcopy}")
