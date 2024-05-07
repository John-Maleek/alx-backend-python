#!/usr/bin/env python3
"""
    Module defines coroutine called
    async_comprehension that takes no arguments.
"""


import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        returns the total time taken to
        completed the operation
    """
    begin: float = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    time_taken: float = time.perf_counter() - begin
    return time_taken
