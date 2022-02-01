#!/usr/bin/env python3
"""write an async routine called wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """calls wait_random and spawns it n times asynchronously"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    time_list = []
    for task in asyncio.as_completed(tasks):
        time: float = await task
        time_list.append(time)
    return time_list
