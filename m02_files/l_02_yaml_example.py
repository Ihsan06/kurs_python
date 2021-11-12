from l_00_inventory import inventory
import yaml

# Convert inventory into Yaml and write to file
with open("l_00_inventory.yaml", "w") as yaml_out:
    yaml_out.write(yaml.dump(inventory))

# Read Yaml inventory from file
with open("l_00_inventory.yaml", "r") as yaml_in:
    yaml_inventory = yaml_in.read()

# Print Yaml inventory string
print("l_00_inventory.json file:\n", yaml_inventory)

# Convert Yaml inventory to python, then convert back to string for printing
print("\nYaml pretty version:")
print(yaml.dump(yaml.safe_load(yaml_inventory), indent=4))

# Convert Yaml inventory to python, then convert back to string for printing
print("\nYaml pretty version:")
print(yaml.dump(yaml.safe_load(yaml_inventory), indent=4, default_flow_style=True))

# Compare inventory we read, with original inventory, to make sure they are equivalent
print("\n------ compare saved inventory with original ---------")
saved_inventory = yaml.safe_load(yaml_inventory)
if saved_inventory == inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")

# Read the ALT-formatted Yaml File
with open("l_00_inventory_formatted.yaml", "r") as yaml_in:
    yaml_inventory_alt = yaml_in.read()

# Print ALT-Formatted Yaml inventory string
print("l_00_inventory_formatted.yaml", yaml_inventory_alt)

# Compare inventory we read, with original inventory, to make sure they are equivalent
print("\n----- compare saved inventory with original --------------")
saved_inventory_alt = yaml.safe_load(yaml_inventory_alt)
if saved_inventory_alt == inventory:
    print("-- worked: saved alt-formatted inventory equals original")
else:
    print("-- failed: saved ALT-formatted inventory different from original")
