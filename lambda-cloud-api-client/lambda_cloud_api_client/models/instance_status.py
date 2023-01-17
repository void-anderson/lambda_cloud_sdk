from enum import Enum


class InstanceStatus(str, Enum):
    ACTIVE = "active"
    BOOTING = "booting"
    UNHEALTHY = "unhealthy"
    TERMINATED = "terminated"

    def __str__(self) -> str:
        return str(self.value)
