#!/usr/bin/env python3
"""
    Module defines a function with
    correct duck-typed annotations
"""


from typing import Any, Mapping, Type, TypeVar, Union

T = TypeVar('T')
NoneType = Type[None]


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, NoneType,]) -> Union[Any, T]:
    '''Returns a Union of Any and T'''
    if key in dct:
        return dct[key]
    else:
        return default
