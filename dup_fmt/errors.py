# -------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# --------------------------------------------------------------------------
"""
Define Errors Object for core engine
"""
from typing import Union


class BaseError(Exception):
    """Base Error Object that use for catch any errors statement of
    all step in this package.
    """


class FormatterError(BaseError):
    """Core Base Error object"""


class FormatterNotFound(FormatterError):
    """Error raise for a method not found the config file or data."""


class FormatterTypeError(FormatterError):
    """Error raise for typing does not match or support."""


class FormatterValueError(FormatterError):
    """Error raise for value does not valid"""


class FormatterKeyError(FormatterError):
    """Error raise for key does not exist"""


class FormatterArgumentError(FormatterError):
    """Error raise for a wrong configuration argument.

    >>> FormatterArgumentError(argument='demo', message='does not support')
    FormatterArgumentError("with 'demo', does not support")

    :param argument: argument of this error that raise to client
    :type argument: Union[str, tuple]
    :param message: string message of this error
    :type message: str
    """

    def __init__(self, argument: Union[str, tuple], message: str):
        """Main Initialization that merge the argument and message input values
        with specific content message together like

            `__class__` with `argument`, `message`
        """
        _argument: str = f"{argument!r}"
        if isinstance(argument, tuple):
            _last_arg: str = str(argument[-1])
            _argument: str = (
                (
                    ", ".join(f"{x!r}" for x in argument[:-1])
                    + f", and {_last_arg!r}"
                )
                if len(argument) > 1
                else f"{_last_arg!r}"
            )
        super().__init__(f"with {_argument}, {message}")
