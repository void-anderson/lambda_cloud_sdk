from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.error_code import ErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    """
    Attributes:
        code (ErrorCode): Unique identifier for the type of error
        message (str): Detailed description of the error Example: API key is invalid, expired, or deleted..
        suggestion (Union[Unset, None, str]): Suggestion of possible ways to fix the error. Example: Create a new API
            key and try again..
    """

    code: ErrorCode
    message: str
    suggestion: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code.value

        message = self.message
        suggestion = self.suggestion

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if suggestion is not UNSET:
            field_dict["suggestion"] = suggestion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = ErrorCode(d.pop("code"))

        message = d.pop("message")

        suggestion = d.pop("suggestion", UNSET)

        error = cls(
            code=code,
            message=message,
            suggestion=suggestion,
        )

        return error
