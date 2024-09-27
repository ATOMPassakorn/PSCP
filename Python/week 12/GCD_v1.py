"""GCD_v1"""
def main():
    """GCD_v1"""
    n1 = int(input())
    n2 = int(input())
    while n2:
        n1,n2=n2,n1%n2
    print(n1)
main()
