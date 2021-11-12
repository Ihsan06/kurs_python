device_str = "  r3-L-n7, cisco, catalyst 2960, ios , extra stupid stuff "

# Non List Comprehension way
device = list()
for item in device_str.split(","):
    device.append(item.strip())
print("\ndevice using for loop: \n\t\t", device)

# Simpler List Comprehension
device_info_list = device_str.split(",")
device = [item.strip() for item in device_info_list]
print("\ndevice using simpler list comprehension with conditional:\n\t\t", device)

# List Comprehension
device =[item.strip() for item in device_str.split(",")]
print("\ndevice using list comprehension:\n\t\t", device)

# List Comprehension with Conditional
device = [item.strip() for item in device_str.split(",") if "stupid" not in item]
print("\ndevice using list comprehension with conditional:\n\t\t", device)

device_info = [
    ("name", "r3-L-n7"),
    ("vendor", "cisco"),
    ("model", "catalyst 2968"),
    ("os", "ios"),
]

# Dict Comprehension from List of Tuples
device = {item[0]: item[1] for item in device_info}
print("\ndevice using dict comprehension\n\t\t", device)
print("\ndevice nicely formatted")
for key, value in device.items():
    print(f'{key:>16s} : {value}')

device_info_str = "name:r3-L-n7, vendor:cisco, model:catalyst 2968, os:ios, version:12.1(T)"

# List then Dict Comprehension from String
device_info_pairs = [kv_pair.strip().split(":") for kv_pair in device_info_str.split(",")]
print(f"\n{device_info_pairs}")
device = {item[0]: item[1] for item in device_info_pairs}
print("\ndevice using list and dict comprehension:\n\t\t", device)
print("\ndevice nicely formatted:")
for key, value in device.items():
    print(f"{key:>16s} : {key}")

# Dict Comprehension from String
device = {item.split(":")[0]: item.split(":")[1] for item in device_info_str.split(",")}
print("\ndevice using dict comprehension:\n\t\t", device)
print("\ndevice nicely formatted:")
for key, value in device.items():
    print(f"{key:>16} : {value}")


