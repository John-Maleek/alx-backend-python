#!/usr/bin/env python3
"""
    Module defines a function with
    correct duck-typed annotations
"""


from typing import Any, Sequence, Type, Union


NoneType = Type(None)


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    '''function with correct duck-typed annotations'''
    if lst:
        return lst[0]
    else:
        return None
