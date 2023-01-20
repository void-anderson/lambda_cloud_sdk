import os, sys
import json, uuid
import functools

from collections import OrderedDict

from lambda_cloud_api_client import AuthenticatedClient
from lambda_cloud_api_client.types import Response

from lambda_cloud_api_client.models import (
    InstanceType,
    InstanceTypeSpecs,
    Instance,
    InstanceStatus,
    SshKey,
    Region,
    Error,
    ErrorCode,
    ErrorResponseBody,
)

from lambda_cloud_api_client.api.default import (
    instance_types,
    list_instances,
    list_ssh_keys,
    get_instance,
    launch_instance,
    add_ssh_key,
    terminate_instance,
)


class InstanceTypeWithRegions:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.instance_type = kwargs["instance_type"]
        self.regions = kwargs["regions"]

    def __repr__(self):
        return "{}".format(self.to_dict())

    def to_dict(self):
        return {
            "name": self.name,
            "instance_type": self.instance_type.to_dict(),
            "regions": [region.to_dict() for region in self.regions],
        }

    @classmethod
    def from_dict(cls, src_dict):
        d = src_dict.copy()
        instance_type = d.pop("instance_type")
        regions = d.pop("regions_with_capacity_available")
        name = instance_type["name"]
        instance_type_with_regions = cls(
            name=name,
            instance_type=InstanceType.from_dict(instance_type),
            regions=[Region.from_dict(region) for region in regions],
        )
        return instance_type_with_regions


TypeMap = {
    "instance_type": InstanceType,
    "instance_type_with_regions": InstanceTypeWithRegions,
    "instance": Instance,
    "ssh_key": SshKey,
}


class OPSClient:
    def __init__(self, base_url, access_token):
        self.base_url = base_url
        self.access_token = access_token
        self.debug = int(os.environ.get("DEBUG"))
        self.client = AuthenticatedClient(
            base_url=self.base_url, token=self.access_token
        )

    def _debug(self, msg):
        if self.debug:
            print("DEBUG MSG:{}".format(msg))

    def _parse(self, parsable, type_str):
        res = [TypeMap[type_str].from_dict(item) for item in parsable]
        self._debug(res)
        return res

    def _parse_single(self, parsable, type_str):
        res = TypeMap[type_str].from_dict(parsable)
        self._debug(res)
        return res

    def _list(self, api, type_str):
        response = api.sync_detailed(client=self.client)
        data = json.loads(response.content)["data"]
        parsable = data.values() if type(data) is dict else data
        self._debug(response.status_code)
        return self._parse(parsable, type_str)

    def _get(self, api, id):
        response = api.sync_detailed(client=self.client, id=id)
        self._debug(response.status_code)
        data = json.loads(response.content)["data"]
        return self._parse_single(data, "instance")

    def _exclusive_kw(self, kw, arg_list):
        args = {k: v for k, v in kw.items() if k in arg_list}
        return args

    def _apply_filters(self, parsed, filters):
        for _filter in filters:
            parsed = list(filter(_filter, parsed))
        return parsed

    def list_instance_types(self, filters=[]):
        parsed = self._list(instance_types, "instance_type_with_regions")
        return self._apply_filters(parsed, filters)

    def list_instances(self, filters=[]):
        parsed = self._list(list_instances, "instance")
        return self._apply_filters(parsed, filters)

    def list_ssh_keys(self, filters=[]):
        parsed = self._list(list_ssh_keys, "ssh_key")
        return self._apply_filters(parsed, filters)

    def get_instance(self, id):
        return self._get(get_instance, id)

    def create_instances(self, **kwargs):
        args = self._exclusive_kw(
            kwargs,
            [
                "region_name",
                "instance_type_name",
                "ssh_key_names",
                "file_system_names",
                "quantity",
                "name",
            ],
        )
        args["name"] = args["name"] if "name" in args.keys() else uuid.uuid4().hex
        print(args)
        response = launch_instance.sync_detailed(client=self.client, **args)
        self._debug(response.status_code)
        data = json.loads(response.content)["data"]
        return data["instance_ids"]

    def remove_instance(self):
        pass

    def create_ssh_key(self, name=None):
        name = name if name else uuid.uuid4().hex
        response = add_ssh_key.sync_detailed(client=self.client, name=name)
        self._debug(response.status_code)
        data = json.loads(response.content)["data"]
        return self._parse_single(data, "ssh_key")
