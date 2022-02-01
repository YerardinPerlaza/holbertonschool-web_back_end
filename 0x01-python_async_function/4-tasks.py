#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """calls wait_random and spawns it n times asynchronously"""
    time_list = []
    for _ in range(n):
        time_list.append(task_wait_random(max_delay))
    return [await time for time in asyncio.as_completed(time_list)]
