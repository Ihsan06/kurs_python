from pprint import pprint

# DICTIONARY representing a Device
device = {
    "name": "abc1223",
    "vendor": "cisco",
    "model": "classicabc",
    "os": "nxos",
    "version": "1.2.3",
    "ip": "1.2.3.4.5.6",
}

# SIMPLE PRINT
print('\n________SIMPLE PRINT_______')
print("device:", device)
print("device name:", device["name"])

# PRETTY PRINT
print("\n_____PRETTY PRINT_____")
pprint(device)

# FOR LOOP, NICELY FORMATTED PRINT
print("\n_____FOR LOOP, USING F-STRING______")
for key, value in device.items():
    print(f"{key:>16s} : {value:}")
