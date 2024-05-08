#!/usr/bin/env python3
"""
    Module defines coroutine called
    async_generator that takes no arguments
"""


import asyncio
import random
from typing import Any, Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    '''function yield a random value'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
