#!/usr/bin/env python3
"""Measure runtime of async_comprehension"""
async_comprehension = __import__('1-async_comprehension').async_comprehension
import time
import asyncio


async def measure_runtime() -> float:
    """
    Executes 'async_comprehension' 4 times
    and returns the time took to run
    """
    start: float = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(*tasks)
    return (time.time() - start)
