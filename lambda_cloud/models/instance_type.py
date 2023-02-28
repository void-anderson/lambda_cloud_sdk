from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.instance_type_specs import InstanceTypeSpecs


T = TypeVar("T", bound="InstanceType")


@attr.s(auto_attribs=True)
class InstanceType:
    """Hardware configuration and pricing of an instance type

    Attributes:
        name (str): Name of an instance type Example: gpu_1x_a100.
        description (str): Long name of the instance type Example: 1x RTX A100 (24 GB).
        price_cents_per_hour (int): Price of the instance type, in US cents per hour Example: 110.
        specs (InstanceTypeSpecs):
    """

    name: str
    description: str
    price_cents_per_hour: int
    specs: "InstanceTypeSpecs"

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        price_cents_per_hour = self.price_cents_per_hour
        specs = self.specs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "description": description,
                "price_cents_per_hour": price_cents_per_hour,
                "specs": specs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.instance_type_specs import InstanceTypeSpecs

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        price_cents_per_hour = d.pop("price_cents_per_hour")

        specs = InstanceTypeSpecs.from_dict(d.pop("specs"))

        instance_type = cls(
            name=name,
            description=description,
            price_cents_per_hour=price_cents_per_hour,
            specs=specs,
        )

        return instance_type
