#!/usr/bin/env python3
"""
    Module defines coroutine called
    async_generator that takes no arguments
"""


import asyncio
import random
from typing import Any, AsyncGenerator


async def async_generator() -> AsyncGenerator[Any, Any]:
    '''function yield a random value'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
