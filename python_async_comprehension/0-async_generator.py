#!/usr/bin/env python3
"""async_generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loop 10 times. In each iteration, wait 1 second, then
    yield a random num between 0 & 10 using random module
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
