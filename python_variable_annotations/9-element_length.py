#!/usr/bin/env python3
"""annotate functions params and
return values with appropraite types"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return a list of tuples that is a sequence on ints"""
    return [(i, len(i)) for i in lst]
