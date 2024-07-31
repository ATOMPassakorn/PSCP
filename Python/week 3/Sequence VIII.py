"""Sequence VIII"""
def main():
    """Sequence VIII"""
    num = int(input())
    for i in range(1,num+1):
        print(" "*(3*(num-1)),end="")
        num-=1
        for j in range(1,i+1):
            print(f"{j:>02}",end=" ")
        print()
main()
