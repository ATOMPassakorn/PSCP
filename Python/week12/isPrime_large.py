"""isprime_small"""
def is_prime(num):
    """prime"""
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if not num%i:
            return False
    return True
def main():
    """isprime_small"""
    num=int(input())
    if is_prime(num):
        print("YES")
    else:
        print("NO")
main()
