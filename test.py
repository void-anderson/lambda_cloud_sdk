import os
from client import OPSClient

BASE_URL = os.environ.get("BASE_URL")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

opsc = OPSClient(BASE_URL, ACCESS_TOKEN)


# # Instance Types
# instance_types = opsc.list_instance_types(
#     lambda i: len(i["regions_with_capacity_available"]) > 0
# )
# instances = opsc.list_instances()
#
# # With SSH Keys
# ssh_key = opsc.create_ssh_key()
# ssh_keys = opsc.list_ssh_keys()
#
#
# # Print the results
# print(instance_types)
# print(instances)
#
# print(ssh_key)
# print(ssh_keys)

instance = opsc.create_instance(region_name="hello")
