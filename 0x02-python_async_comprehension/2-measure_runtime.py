#!/usr/bin/env python3
"""write a coroutine called async_comprehension"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel using asyncio.gather,
    should measure total runtime and return it"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    total_time = time.perf_counter() - start
    return total_time
