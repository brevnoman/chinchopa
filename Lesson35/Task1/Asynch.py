import asyncio
import time

"""
this code did it 10 time's faster, idk why
"""

async def fibonacci(indexes_of_fibonacci: list):
    result_list = []
    for num in indexes_of_fibonacci:
        current = 1
        previous = 0
        result = 0
        for _ in range(num):
            result = current + previous
            current, previous = current + previous, current
        result_list.append(result)
    return result_list

async def factorial(nums:list):
    result_list = []
    for num in nums:
        start = 1
        result = 1
        for i in range(num):
            result = start * result
            start += 1
        result_list.append(result)
    return result_list

async def squares(nums: list):
    result = []
    for num in nums:
        result.append(num**2)
    return result

async def cubic(nums: list):
    result = []
    for num in nums:
        result.append(num ** 3)
    return result


async def do_things(nums: list):
    t1 = asyncio.create_task(fibonacci(nums))
    t2 = asyncio.create_task(factorial(nums))
    t3 = asyncio.create_task(squares(nums))
    t4 = asyncio.create_task(cubic(nums))
    await asyncio.gather(t1,t2,t3,t4)

    print(t1.result(), "fibonacci\n", t2.result(), "factorial\n", t3.result(), "squares\n", t4.result(), "cubic")

if __name__ == '__main__':
    start = time.time()
    asyncio.run(do_things([1,2,3,4,5]))
    print(start - time.time())
