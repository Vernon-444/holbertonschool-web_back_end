#!/usr/bin/env python3
"""Takes a list mxd_lst of floats as arg,
returns their sums as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum floats and ints """
    return sum(mxd_lst)
