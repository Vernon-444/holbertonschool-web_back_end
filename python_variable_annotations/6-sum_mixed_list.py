#!/usr/bin/env python3
"""Takes a list mxd_lst of floats as arg,
returns their sums as a float
"""
from typing import List


def sum_mixed_list(mxd_lst: List[float]) -> float:
    """ return the sum of the list """
    return float(sum((mxd_lst)))
