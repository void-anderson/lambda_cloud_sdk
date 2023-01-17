from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.error import Error


T = TypeVar("T", bound="ErrorResponseBody")


@attr.s(auto_attribs=True)
class ErrorResponseBody:
    """
    Attributes:
        error (Error):
    """

    error: "Error"

    def to_dict(self) -> Dict[str, Any]:
        error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error

        d = src_dict.copy()
        error = Error.from_dict(d.pop("error"))

        error_response_body = cls(
            error=error,
        )

        return error_response_body
