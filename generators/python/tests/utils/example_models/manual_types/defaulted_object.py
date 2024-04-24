import datetime as dt
import typing

from core_utilities.sdk.unchecked_base_model import UncheckedBaseModel
from core_utilities.sdk.pydantic_utilities import pydantic_v1


class ObjectWithDefaultedOptionalFields(UncheckedBaseModel):
    literal_: typing.Optional[typing.Literal["lit_one", "lit_two"]] = pydantic_v1.Field(alias="literal", default="lit_one")
    string: typing.Optional[str] = None
    integer: typing.Optional[int] = None
    long_: typing.Optional[int] = pydantic_v1.Field(alias="long", default=200000)
    double: typing.Optional[float] = None
    bool_: typing.Optional[bool] = pydantic_v1.Field(alias="bool", default=True)
    datetime: typing.Optional[dt.datetime] = None
    date: typing.Optional[dt.date] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow