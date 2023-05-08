#!/usr/bin/env python3
"""takes string k and an int/float v as arg and returns tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ first element of tuple is str k. Second
element is square of int/float v and annotated as float"""
    return (k, v * v)
