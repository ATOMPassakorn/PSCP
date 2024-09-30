"""FibonacciRecursionV2"""
fibo_cache = {0: 0, 1: 1}
def fibo(num):
    """Calculate Fibonacci with memoization"""
    if num in fibo_cache:
        return fibo_cache[num]
    value = fibo(num - 1) + fibo(num - 2)
    fibo_cache[num] = value
    return value
def calculate_fib(start, end):
    """Calculate Fibonacci with manual loop"""
    if start > end:
        return []
    results = []
    results.append(fibo(start))
    return results + calculate_fib(start + 1, end)
def batch_fib(start, end, batch_size):
    """Calculate Fibonacci with manual loop"""
    if start > end:
        return []
    results = calculate_fib(start, min(start + batch_size - 1, end))
    return results + batch_fib(start + batch_size, end, batch_size)
def ans():
    """Find ans"""
    num = int(input())
    batch_size = 980
    results = batch_fib(0, num, batch_size)
    print(results[-1])
ans()
