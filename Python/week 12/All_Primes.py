"""All_Primes"""
def is_prime(num):
    """prime"""
    if num<2:
        return False
    if num==2:
        return True
    for i in range(2,num):
        if not num%i:
            return False
    return True
def number():
    """find number"""
    n=int(input())
    counts = 0
    for num in range(1,n+1):
        if is_prime(num):
            counts +=1
        else:
            counts +=0
    print(counts)
number()
