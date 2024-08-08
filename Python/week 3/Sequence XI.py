"""Sequence XI"""
def main():
    """Sequence XI"""
    n=int(input())
    size=2*n
    for i in range(1,size):
        for j in range(1,size):
            number=min(i,j,n,2*n-i,2*n-j)
            print(f"{number:02}",end=" ")
        print()
main()
