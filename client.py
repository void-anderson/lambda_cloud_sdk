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


TypeMap = {
    "instance_type": InstanceType,
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
        model_collection = list()
        for item in parsable:
            dict_item = item[type_str] if type_str in ["instance_type"] else item
            model_collection.append(TypeMap[type_str].from_dict(dict_item))
        res = {"raw": parsable, "collection": model_collection}
        self._debug(res)
        return res

    def _parse_single(self, parsable, type_str):
        model = TypeMap[type_str].from_dict(parsable)
        res = {"raw": parsable, "model": model}
        self._debug(res)
        return res

    def _list(self, api, type_str, _filter=None):
        response = api.sync_detailed(client=self.client)
        data = json.loads(response.content)["data"]
        parsable = data.values() if type_str in ["instance_type"] else data
        if _filter:
            parsable = list(filter(_filter, parsable))
        self._debug(response.status_code)
        return self._parse(parsable, type_str)

    def _get(self, api, id):
        response = api.sync_detailed(client=self.client, id=id)
        return self._parse(response)

    def _exclusive_kw(self, kw, arg_list):
        args = {k: v for k, v in kw.items() if k in arg_list}
        return args

    def list_instance_types(self, _filter=None):
        return self._list(instance_types, "instance_type", _filter)

    def list_instances(self, _filter=None):
        return self._list(list_instances, "instance", _filter)

    def list_ssh_keys(self, _filter=None):
        return self._list(list_ssh_keys, "ssh_key", _filter)

    def get_instance(self, id):
        return self._get(get_instance, id)

    def create_instance(self, **kwargs):
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
        print(args)
        response = launch_instance.sync_detailed(client=self.client, **args)
        print(response)

    def remove_instance(self):
        pass

    def create_ssh_key(self, name=None):
        name = name if name else uuid.uuid4().hex
        response = add_ssh_key.sync_detailed(client=self.client, name=name)
        data = json.loads(response.content)["data"]
        return self._parse_single(data, "ssh_key")
