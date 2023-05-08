#!/usr/bin/env python3
"""Takes wait random from task 0, add another routine"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple routines with async"""
    listDelay = [wait_random(max_delay) for i in range(n)]
    inOrder = []
    for delay in asyncio.as_completed(listDelay):
        inOrder.append(await delay)
    return inOrder
