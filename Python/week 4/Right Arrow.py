"""Right Arrow"""
def main():
    """Right Arrow"""
    k=int(input())
    n=int(input())
    up=n//2
    down=0
    for _ in range(n//2):
        print(" "*(down),end="")
        print("*"*k,end="")
        down+=1
        print()
    for _ in range(1,up+2):
        print(" "*(up),end="")
        print("*"*k,end="")
        up-=1
        print()
main()
