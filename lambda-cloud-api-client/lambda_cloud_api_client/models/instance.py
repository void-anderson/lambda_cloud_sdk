from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.instance_status import InstanceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instance_type import InstanceType
    from ..models.region import Region


T = TypeVar("T", bound="Instance")


@attr.s(auto_attribs=True)
class Instance:
    """Virtual machine (VM) in Lambda Cloud

    Attributes:
        id (str): Unique identifier (ID) of an instance Example: 0920582c7ff041399e34823a0be62549.
        status (InstanceStatus): The current status of the instance
        ssh_key_names (List[str]): Names of the SSH keys allowed to access the instance
        file_system_names (List[str]): Names of the file systems, if any, attached to the instance
        name (Union[Unset, None, str]): User-provided name for the instance Example: training-node-1.
        ip (Union[Unset, None, str]): IPv4 address of the instance Example: 10.10.10.1.
        region (Union[Unset, Region]):
        instance_type (Union[Unset, InstanceType]): Hardware configuration and pricing of an instance type
        hostname (Union[Unset, None, str]): Hostname assigned to this instance, which resolves to the instance's IP.
            Example: 10-0-8-196.cloud.lambdalabs.com.
        jupyter_token (Union[Unset, None, str]): Secret token used to log into the jupyter lab server hosted on the
            instance. Example: 53968f128c4a4489b688c2c0a181d083.
        jupyter_url (Union[Unset, None, str]): URL that opens a jupyter lab notebook on the instance. Example:
            https://jupyter-3ac4c5c6-9026-47d2-9a33-71efccbcd0ee.lambdaspaces.com/?token=53968f128c4a4489b688c2c0a181d083.
    """

    id: str
    status: InstanceStatus
    ssh_key_names: List[str]
    file_system_names: List[str]
    name: Union[Unset, None, str] = UNSET
    ip: Union[Unset, None, str] = UNSET
    region: Union[Unset, "Region"] = UNSET
    instance_type: Union[Unset, "InstanceType"] = UNSET
    hostname: Union[Unset, None, str] = UNSET
    jupyter_token: Union[Unset, None, str] = UNSET
    jupyter_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status.value

        ssh_key_names = self.ssh_key_names

        file_system_names = self.file_system_names

        name = self.name
        ip = self.ip
        region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        instance_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.instance_type, Unset):
            instance_type = self.instance_type.to_dict()

        hostname = self.hostname
        jupyter_token = self.jupyter_token
        jupyter_url = self.jupyter_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "ssh_key_names": ssh_key_names,
                "file_system_names": file_system_names,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if region is not UNSET:
            field_dict["region"] = region
        if instance_type is not UNSET:
            field_dict["instance_type"] = instance_type
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if jupyter_token is not UNSET:
            field_dict["jupyter_token"] = jupyter_token
        if jupyter_url is not UNSET:
            field_dict["jupyter_url"] = jupyter_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.instance_type import InstanceType
        from ..models.region import Region

        d = src_dict.copy()
        id = d.pop("id")

        status = InstanceStatus(d.pop("status"))

        ssh_key_names = cast(List[str], d.pop("ssh_key_names"))

        file_system_names = cast(List[str], d.pop("file_system_names"))

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, Region]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Region.from_dict(_region)

        _instance_type = d.pop("instance_type", UNSET)
        instance_type: Union[Unset, InstanceType]
        if isinstance(_instance_type, Unset):
            instance_type = UNSET
        else:
            instance_type = InstanceType.from_dict(_instance_type)

        hostname = d.pop("hostname", UNSET)

        jupyter_token = d.pop("jupyter_token", UNSET)

        jupyter_url = d.pop("jupyter_url", UNSET)

        instance = cls(
            id=id,
            status=status,
            ssh_key_names=ssh_key_names,
            file_system_names=file_system_names,
            name=name,
            ip=ip,
            region=region,
            instance_type=instance_type,
            hostname=hostname,
            jupyter_token=jupyter_token,
            jupyter_url=jupyter_url,
        )

        instance.additional_properties = d
        return instance

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
