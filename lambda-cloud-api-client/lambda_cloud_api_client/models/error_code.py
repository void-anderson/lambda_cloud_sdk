from enum import Enum


class ErrorCode(str, Enum):
    GLOBALUNKNOWN = "global/unknown"
    GLOBALINVALID_API_KEY = "global/invalid-api-key"
    GLOBALACCOUNT_INACTIVE = "global/account-inactive"
    GLOBALINVALID_PARAMETERS = "global/invalid-parameters"
    GLOBALOBJECT_DOES_NOT_EXIST = "global/object-does-not-exist"
    INSTANCE_OPERATIONSLAUNCHINSUFFICIENT_CAPACITY = "instance-operations/launch/insufficient-capacity"
    INSTANCE_OPERATIONSLAUNCHFILE_SYSTEM_IN_WRONG_REGION = "instance-operations/launch/file-system-in-wrong-region"
    INSTANCE_OPERATIONSLAUNCHFILE_SYSTEMS_NOT_SUPPORTED = "instance-operations/launch/file-systems-not-supported"

    def __str__(self) -> str:
        return str(self.value)
