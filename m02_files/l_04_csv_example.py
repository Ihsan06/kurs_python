from l_00_inventory import csv_inventory
import csv
from pprint import pprint
from tabulate import tabulate
import filecmp

# Part 1: ---- Same procedure as for JSON, YAML, XML ---------

# Convert inventory to csv and write to file
with open("l_00_inventory.csv", "w") as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerows(csv_inventory)

# Read csv inventory from file
with open("l_00_inventory.csv", "r") as csv_in:
    csv_reader = csv.reader(csv_in)
    saved_csv_inventory = list()
    for device in csv_reader:
        saved_csv_inventory.append(device)

# Print csv inventory string
print("l_inventory.csv file:\n", saved_csv_inventory)

# Pretty print
print("\ncsv pretty print version:")
pprint(saved_csv_inventory)

# Compare inventory we read, with original inventory, to make sure they are equivalent
print("\n---- compare saved inventory with original -----------")
if saved_csv_inventory == csv_inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")

# Turn lists into dict
devices = list()
for device_index in range(1, len(csv_inventory)):
    device = dict()
    for index, header in enumerate(csv_inventory[0]):
        device[header] = csv_inventory[device_index][index]
    devices.append(device)

# Pretty print devices as list od dicts
print(f"\n----- Devices as list of dicts")
pprint(device)

# Part II: ------ Read csv file created by spreadsheet ----------

# Read from csv file created by spreadsheet
with open("devices_for_csv_example - Sheet1.csv", "r") as csv_in:
    csv_reader = csv.reader(csv_in)
    from_spreadsheet_csv_inventory = list()
    for device in csv_reader:
        from_spreadsheet_csv_inventory.append(device)

# Turn list of lists into dict
devices = list()
for device_index in range(1, len(from_spreadsheet_csv_inventory)):
    device = dict()
    for index, header in enumerate(from_spreadsheet_csv_inventory[0]):
        device[header] = from_spreadsheet_csv_inventory[device_index][index]
    devices.append(device)

# Pretty print devices as list od dicts
print("\n----- Devices from spreadsheet -------------")
pprint(devices)

print("\n----- tabulate output of devices from spreadsheet")
print("\n", tabulate(devices, headers="keys"))

# Convert python data back into csv
headers = devices[0].keys()
with open("l_00_inventory_back_to_csv.csv", "w") as csv_out:
    csv_writer = csv.DictWriter(csv_out, headers)
    csv_writer.writeheader()
    csv_writer.writerows(devices)

print("\n---- compare spreadsheet data with our version ------------")
if filecmp.cmp("devices_for_csv_example - Sheet1.csv", "l_00_inventory_back_to_csv.csv"):
    print("-- worked: spreadsheet devices equals our version")
else:
    print("-- failed: But expected to fail: spreadsheet devices different from our version")
