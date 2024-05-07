#!/usr/bin/env python3
"""
    Module defines coroutine called
    async_comprehension that takes no arguments.
"""


import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
        returns a list of random values
        generated by the async_generator
    """
    random_nums: List[int] = [i async for i in async_generator()]
    return random_nums