from basic_async_syntax import wait_random
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create and run n asynchronous tasks that each wait for a random delay up to max_delay.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay each task will wait for.

    Returns:
        List[float]: A list of results from each task, which are the delays (float) for demonstration.
    """
    tasks: List[asyncio.Task] = []
    
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
        
    results: List[float] = await asyncio.gather(*tasks)
    
    return results

    


