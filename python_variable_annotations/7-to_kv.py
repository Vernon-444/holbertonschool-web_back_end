#!/usr/bin/env python3
"""takes string k and an int/float v as arg and returns tuple"""
from typing import Tuple


def to_kv(k: str, v: float) -> Tuple[str, float]:
    """return tuple (k, v)"""
    return (k, v * v)
