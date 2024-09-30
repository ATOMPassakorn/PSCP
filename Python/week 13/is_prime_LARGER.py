"""isprime_LARGER"""
def is_prime(num):
    """prime"""
    if num<=1:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if not num%i:
            return False
    return True
def main():
    """isprime_LARGER"""
    num=int(input())
    if is_prime(num):
        print("True")
    else:
        print("False")
main()
