#!/usr/bin/env python3
"""Module defines an asynchronous coroutine"""


from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
        Returns an aray of the delays
    '''
    delays: List[float] = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))

    return sorted([await delay for delay in delays], reverse=False)
