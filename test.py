import os
from client import OPSClient

BASE_URL = os.environ.get("BASE_URL")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

opsc = OPSClient(BASE_URL, ACCESS_TOKEN)


# Instance Types
returned_instance_types = opsc.list_instance_types()
returned_instances = opsc.list_instances()

# With SSH Keys
returned_ssh_key = opsc.create_ssh_key()
returned_ssh_keys = opsc.list_ssh_keys()

print(returned_instance_types)
print(returned_instances)

print(returned_ssh_key)
print(returned_ssh_keys)

# for keys in returned_instance_types["data"]:
# v = returned_instance_types["data"][keys]
# capable_regions = v["regions_with_capacity_available"]
# if len(capable_regions) != 0:
#    print(v)
