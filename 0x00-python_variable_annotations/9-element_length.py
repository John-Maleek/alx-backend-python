#!/usr/bin/env python3
"""
    Module defines an annotated function
"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """
        returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
