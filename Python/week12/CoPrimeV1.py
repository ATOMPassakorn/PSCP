"""CoPrimeV1"""
import math
def main():
    """CoPrimeV1"""
    n1 = int(input())
    n2 = int(input())
    x = math.gcd(n1,n2)
    if x ==1:
        print("YES")
        print(x)
    else:
        print("NO")
        print(x)
main()
