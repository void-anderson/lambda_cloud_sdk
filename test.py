import os
from client import OPSClient

BASE_URL = os.environ.get("BASE_URL")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

opsc = OPSClient(BASE_URL, ACCESS_TOKEN)

# Instance Types
print("listing available instance types...")
instance_types = opsc.list_instance_types(
    [
        lambda i: len(i.regions) > 0,
        lambda i: i.instance_type.price_cents_per_hour < 100,
    ]
)
print("listing running instances...")
instances = opsc.list_instances()

# With SSH Keys
print("creating ssh key...")
ssh_key = opsc.create_ssh_key()
print("listing available ssh keys...")
ssh_keys = opsc.list_ssh_keys()

# Print the results
print(instance_types)
print(instances)
#
print(ssh_key)
print(ssh_keys)

# instance = opsc.create_instance(region_name="hello")
