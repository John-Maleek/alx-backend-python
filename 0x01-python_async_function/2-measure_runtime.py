#!/usr/bin/env python3
"""Module defines an asynchronous coroutine"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    '''
        Returns the time per run of the wait_n function
    '''
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_taken: float = time.perf_counter() - start_time

    return time_taken / n
