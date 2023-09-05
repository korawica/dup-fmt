# -------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# --------------------------------------------------------------------------

from .__about__ import (
    __version__,
    __version_tuple__,
)
from .exceptions import (
    FormatterArgumentError,
    FormatterError,
    FormatterKeyError,
    FormatterNotFoundError,
    FormatterTypeError,
    FormatterValueError,
)
from .formatter import (
    Constant,
    ConstantType,
    Datetime,
    EnvConstant,
    # Formatter
    Formatter,
    # Formatter Group
    FormatterGroup,
    FormatterGroupType,
    FormatterType,
    Naming,
    ReturnFormattersType,
    ReturnPrioritiesType,
    Serial,
    Version,
    dict2const,
    fmt2const,
    make_const,
    make_group,
)
from .objects import (
    relativeserial,
)

__all__ = (
    "relativeserial",
    # ---
    # Formatter
    "Formatter",
    "FormatterType",
    "ReturnPrioritiesType",
    "ReturnFormattersType",
    "Serial",
    "Datetime",
    "Version",
    "Naming",
    "ConstantType",
    "Constant",
    "EnvConstant",
    "fmt2const",
    "dict2const",
    "make_const",
    # Formatter Group
    "FormatterGroup",
    "FormatterGroupType",
    "make_group",
    # ---
    "FormatterArgumentError",
    "FormatterError",
    "FormatterKeyError",
    "FormatterNotFoundError",
    "FormatterTypeError",
    "FormatterValueError",
    # ---
    "__version__",
    "__version_tuple__",
)
