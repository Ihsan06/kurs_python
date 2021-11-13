from l_00_inventory import inventory
import json

# Convert inventory into json and write to file
with open("l_00_inventory.json", "w") as json_out:
    json_out.write(json.dumps(inventory, indent=4))

# Read Json inventory from file
with open("l_00_inventory.json", "r") as json_in:
    json_inventory = json_in.read()

# Print Json inventory string
print("l_00_inventory.json file:", json_inventory)

# Convert json inventory to python, then convert back to string for printing
print("\njson pretty version:")
print(json.dumps(json.loads(json_inventory), indent=4))

# Compare inventory we read, with original inventory, to make sure they are equivalent
print("\n------ compare saved inventory with original ---------")
saved_inventory = json.loads(json_inventory)
if saved_inventory == inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from originalTEST")
