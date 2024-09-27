"""GCD_v2"""
def main():
    """GCD_v2"""
    n1 = int(input())
    n2 = int(input())
    while n2:
        old=n1
        n1=n2
        n2=old%n2
    print(n1)
main()
