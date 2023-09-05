# Data Utility Package: *Formatter*

[![test](https://github.com/korawica/dup-fmt/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/korawica/dup-fmt/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/korawica/dup-fmt/branch/main/graph/badge.svg?token=J2MN63IFT0)](https://codecov.io/gh/korawica/dup-fmt)
[![python support version](https://img.shields.io/pypi/pyversions/dup-fmt)](https://pypi.org/project/dup-fmt/)
[![size](https://img.shields.io/github/languages/code-size/korawica/dup-fmt)](https://github.com/korawica/dup-fmt)

**Type**: `DUP` | **Tag**: `Data Utility Package` `Data` `Utility` `Formatter`

**Table of Contents**:

- [Formatter Objects](#formatter-objects)
  - [Datetime](#datetime)
  - [Version](#version)
  - [Serial](#serial)
  - [Naming](#naming)
  - [Storage](#storage)
  - [Constant](#constant)
- [Formatter Group](#formatter-group)
- [Custom Formatter Object](#custom-formatter-object)

This **Formatter** package was created for `parse` and `format` any string values
that match format pattern with Python regular expression. This package be the
co-pylot project for stating to my **Python Software Developer** role.

**Install from PyPI**:

```shell
pip install dup-fmt
```

:dart: First objective of this project is include necessary formatter objects for
any data components package which mean we can `parse` any complicate names on
data source and ingest the right names to in-house or data target.

For example, we want to get filename with the format like, `filename_20220101.csv`,
on the file system storage, and we want to incremental ingest the latest file with
date **2022-03-25** date. So we will implement `Datetime` object and parse
that filename to it,

```python
Datetime.parse('filename_20220101.csv', 'filename_%Y%m%d.csv').value == datetime.today()
```

The above example is :yawning_face: **NOT SURPRISE!!!** for us because Python
already provide build-in package `datetime` to parse by `{dt}.strptime` and
format by `{dt}.strftime` with any datetime string value. This package will the
special thing when we group more than one formatter objects together as
`Naming`, `Version`, and `Datetime`.

**For complex filename format like**:

```text
{filename:%s}_{datetime:%Y_%m_%d}.{version:%m.%n.%c}.csv
```

From above filename format string, the `datetime` package does not enough for
this scenario right? but you can handle by your hard-code object or create the
better package than this project.

> **Note**: \
> Any formatter object was implemented the `self.valid` method for help us validate
> target string value like the above example scenario,
> ```python
> this_date = Datetime.parse('20220101', '%Y%m%d')
> this_date.valid('any_files_20220101.csv', 'any_files_%Y%m%d.csv')  # True
> ```

## Formatter Objects

- [Datetime](#datetime)
- [Version](#version)
- [Serial](#serial)
- [Naming](#naming)
- [Constant](#constant)

The main purpose is **Formatter Objects** for `parse` and `format` with string
value, such as `Datetime`, `Version`, and `Serial` formatter objects. These objects
were used for parse any filename with put the format string value. The formatter
able to enhancement any format value from sting value, like in `Datetime`, for `%B`
value that was designed for month shortname (`Jan`, `Feb`, etc.) that does not
support in build-in `datetime` package.

> **Note**: \
> The main usage of this formatter object is `parse` and `format` method.

### Datetime

```python
from dup_fmt import Datetime

datetime = Datetime.parse(
   value='This_is_time_20220101_000101',
   fmt='This_is_time_%Y%m%d_%H%M%S'
)
datetime.format('This_datetime_format_%Y%b-%-d_%H:%M:%S')
```

```text
>>> 'This_datetime_format_2022Jan-1_00:01:01'
```

[Supported Datetime formats](/docs/en/docs/API.md#datetime)

### Version

```python
from dup_fmt import Version

version = Version.parse(
    value='This_is_version_2_0_1',
    fmt='This_is_version_%m_%n_%c',
)
version.format('New_version_%m%n%c')
```

```text
>>> 'New_version_201'
```

[Supported Version formats](/docs/en/docs/API.md#version)

### Serial

```python
from dup_fmt import Serial

serial = Serial.parse(
    value='This_is_serial_62130',
    fmt='This_is_serial_%n'
)
serial.format('Convert to binary: %b')
```

```text
>>> 'Convert to binary: 1111001010110010'
```

[Supported Serial formats](/docs/en/docs/API.md#serial)

### Naming

```python
from dup_fmt import Naming

naming = Naming.parse(
    value='de is data engineer',
    fmt='%a is %n'
)
naming.format('Camel case is %c')
```

```text
>>> 'Camel case is dataEngineer'
```

[Supported Naming formats](/docs/en/docs/API.md#naming)

### Storage

```python
from dup_fmt import Storage

storage = Storage.parse(
    value='This file have 250MB size',
    fmt='This file have %M size'
)
storage.format('The byte size is: %b')
```

```text
>>> 'The byte size is: 2097152000'
```

[Supported Storage formats](/docs/en/docs/API.md#storage)

### Constant

```python
from dup_fmt import Constant, make_const
from dup_fmt.exceptions import FormatterError

const = make_const({
    '%n': 'normal',
    '%s': 'special',
})
try:
    parse_const: Constant = const.parse(
        value='This_is_constant_normal',
        fmt='This_is_constant_%n'
    )
    parse_const.format('The value of %%s is %s')
except FormatterError as err:
    print(err)
```

```text
>>> 'The value of %s is special'
```

> **Note**: \
> This package already implement environment constant object, `dup_fmt.EnvConstant`.

## Formatter Group

The **Formatter Group** object, `FormatterGroup`, which is the grouping of needed
mapping formatter objects and its name together. You can define a name of formatter
that you want, like `name` for `Naming` object, or `timestamp` for `Datetime` object.

**Parse**:

```python
from dup_fmt import make_group, Naming, Datetime

group = make_group({'name': Naming, 'datetime': Datetime})
group.parse(
    'data_engineer_in_20220101_de',
    fmt='{name:%s}_in_{timestamp:%Y%m%d}_{name:%a}'
)
```

```text
>>> {
>>>     'name': Naming.parse('data engineer', '%n'),
>>>     'timestamp': Datetime.parse('2022-01-01 00:00:00.000000', '%Y-%m-%d %H:%M:%S.%f')
>>> }
```

**Format**:

```python
from dup_fmt import FormatterGroup
from datetime import datetime

group_01: FormatterGroup = group({
    'name': 'data engineer',
    'datetime': datetime(2022, 1, 1)
})
group_01.format('{name:%c}_{timestamp:%Y_%m_%d}')
```

```text
>>> dataEngineer_2022_01_01
```

## Custom Formatter Object

If this implemented formatter objects in this package does not help you all scenario
of a formatted value, you can create your formatter object by yourself.

This package provide the base abstract class, `Formatter`, for this use-case. You
can create your formatter object like,

```python
from typing import Optional
from dup_fmt import Formatter, ReturnPrioritiesType, ReturnFormattersType


class Storage(Formatter):

    base_fmt = '%b'

    __slots__ = (
        "bit",
        "byte",
        "storge",
    )

    @property
    def value(self) -> int:
        return int(self.string)

    @property
    def string(self) -> str:
        return self.bit

    @property
    def validate(self) -> bool:
        if (
            self.bit != 0
            and self.byte != 0
            and self.bit != self.byte
        ):
            return False
        if self.bit == 0 and self.byte != 0:
            self.bit = self.byte
        elif self.bit != 0 and self.byte == 0:
            self.byte = self.bit
        return True

    @property
    def priorities(self) -> ReturnPrioritiesType:
        return {
            "bit": {
                "value": lambda x: str(x),
                "level": 1,
            },
            "byte": {
                "value": lambda x: str(int(x.replace('B', '')) * 8),
                "level": 1,
            },
            "bit_default": {"value": self.default("0")},
            "byte_default": {"value": self.default("0")}
        }

    @staticmethod
    def formatter(
            value: Optional[int] = None,
    ) -> ReturnFormattersType:
        """Generate formatter that support mapping formatter,
            %b  : Bit format
            %B  : Byte format
        """
        size: int = value or 0
        return {
            '%b': {
                'value': lambda: str(size),
                "regex": r"(?P<bit>[0-9]*)",
            },
            '%B': {
                'value': lambda: f"{str(round(size / 8))}B",
                'regex': r"(?P<byte>[0-9]*B)",
            }
        }

Storage({'bit': 2000}).format('%B')
```

```text
>>> 250B
```

Read more about [API Document](/docs/en//docs/API.md).

## License

This project was licensed under the terms of the [MIT license](LICENSE).
