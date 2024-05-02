#!/usr/bin/env python3
"""
    Module defines a  type-annotated function
    make_multiplier that takes a float multiplier
    as argument and returns a function that
    multiplies a float by multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    accepts mutltiplier: float
    returns float_multiplier
    """
    def float_multiplier(fl: float):
        return fl * multiplier

    return float_multiplier
