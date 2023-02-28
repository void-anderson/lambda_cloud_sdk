from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="InstanceTypeSpecs")


@attr.s(auto_attribs=True)
class InstanceTypeSpecs:
    """
    Attributes:
        vcpus (int): Number of virtual CPUs Example: 24.
        memory_gib (int): Amount of RAM, in gibibytes (GiB) Example: 800.
        storage_gib (int): Amount of storage, in gibibytes (GiB). Example: 512.
    """

    vcpus: int
    memory_gib: int
    storage_gib: int

    def to_dict(self) -> Dict[str, Any]:
        vcpus = self.vcpus
        memory_gib = self.memory_gib
        storage_gib = self.storage_gib

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "vcpus": vcpus,
                "memory_gib": memory_gib,
                "storage_gib": storage_gib,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vcpus = d.pop("vcpus")

        memory_gib = d.pop("memory_gib")

        storage_gib = d.pop("storage_gib")

        instance_type_specs = cls(
            vcpus=vcpus,
            memory_gib=memory_gib,
            storage_gib=storage_gib,
        )

        return instance_type_specs
