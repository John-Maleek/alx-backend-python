#!/usr/bin/env python3
"""
    Module defines a function with
    correct duck-typed annotations
"""


from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')
NoneType = Optional[None]


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, NoneType,]) -> Union[Any, T]:
    '''Returns a Union of Any and T'''
    if key in dct:
        return dct[key]
    else:
        return default


annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print(("{}: {}".format(k, v)))
