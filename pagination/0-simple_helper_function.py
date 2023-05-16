#!/usr/bin/env python3
"""Simple Helper Function"""
import typing
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing
    a start and end index corresponding to
    the range of the indexes to return in a
    list for those particular pagination params
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
