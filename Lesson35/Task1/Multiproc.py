import time
import multiprocessing


def fibonacci(indexes_of_fibonacci: list, q):
    result_list = []
    for num in indexes_of_fibonacci:
        current = 1
        previous = 0
        result = 0
        for _ in range(num):
            result = current + previous
            current, previous = current + previous, current
        result_list.append(result)
    q.put(f"{result_list} fibonacci")

def factorial(nums:list, q):
    result_list = []
    for num in nums:
        start = 1
        result = 1
        for i in range(num):
            result = start * result
            start += 1
        result_list.append(result)
    q.put(f"{result_list} factorial")

def squares(nums: list, q):
    result = []
    for num in nums:
        result.append(num**2)
    q.put(f"{result} square")

def cubic(nums: list, q):
    result = []
    for num in nums:
        result.append(num ** 3)
    q.put(f"{result} cubic")


if __name__ == '__main__':
    start = time.time()
    q = multiprocessing.Queue()
    processes = [multiprocessing.Process(target = i, args=([1,2,3,4,5], q, )) for i in [fibonacci, factorial, squares, cubic]]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
        print(q.get())
    print(start - time.time())