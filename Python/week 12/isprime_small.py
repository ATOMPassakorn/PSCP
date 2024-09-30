"""isprime_small"""
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
def main():
    """isprime_small"""
    num=int(input())
    if is_prime(num):
        print("Yes")
    else:
        print("No")
main()
