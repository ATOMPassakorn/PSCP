"""FibonacciRecursionV1"""
def fibo(i,a=0,b=1):
    """FibonacciRecursionV1"""
    if not i:
        print(a)
        return
    if i==1:
        print(b)
        return
    fibo(i-1,b,a+b)
def ans():
    """find ans"""
    num=int(input())
    fibo(num)
ans()
