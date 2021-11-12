from tabulate import tabulate
from util.create_utils import create_devices

# -------- Main program -----------
if __name__ == '__main__':

    # 1 devices = util.create_devices(num_devices=4,num_subnets=5)
    devices = create_devices(num_devices=4, num_subnets=5, random_ip=True)
    print("\n", tabulate(devices, headers="keys"))
