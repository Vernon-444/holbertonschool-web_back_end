#!/usr/bin/env python3
"""takes float multiplier as arg and returns a func
that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type annotated func make_multiplier, takes float multiplier
    as arg, returns a func that multiplies a float by multiplier"""
    def mult(num: float):
        return num * multiplier
    return mult
