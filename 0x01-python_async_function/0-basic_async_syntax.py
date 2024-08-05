"""
    This program demonstrates an asynchronous co-routine called wait_random that takes 
    in an integer argument, called max_delay with a default value of 10, that waits for a 
    random delay between 0 and max_delay in seconds and eventually returns it.
"""


import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """
        Wait randomly for max_delay seconds, then return the time waited for
        :param max_delay: Default for amount of time to delay
        :return: The amount of time delayed
    """
    wait_duration: float = random.random() * max_delay
    await asyncio.sleep(wait_duration)
    return wait_duration
    
    
if __name__ == "__main__":
    print(asyncio.run(wait_random()))
