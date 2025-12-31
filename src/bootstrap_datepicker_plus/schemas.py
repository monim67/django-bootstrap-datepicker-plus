"""Datastructures of the package."""

from enum import Enum
from typing import Any, TypeAlias

InputAttrs: TypeAlias = dict[str, Any]
WidgetOptions: TypeAlias = dict[str, bool | int | str | dict[str, str]]


class WidgetVariant(str, Enum):
    """Variants of widgets."""

    date = "date"
    time = "time"
    datetime = "datetime"
    month = "month"
    year = "year"
