#!/usr/bin/env python3
"""Module defines an asynchronous coroutine"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
        Returns an aray of the delays
    '''
    delays: List[float] = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    return sorted([await delay for delay in delays], reverse=False)
