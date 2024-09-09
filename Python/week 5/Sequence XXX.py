"""Sequence xxx"""
def xxx():
    """Sequence xxx"""
    size=int(input())
    number=int(input())
    for i in range(size):
        if not i or i==size-1:
            for _ in range(number):
                print("*"*size,end=" ")
            print()
        else:
            for _ in range(number):
                for j in range(size):
                    if i==j or not j or j in (size-1,size-1-i):
                        print("*",end="")
                    else:
                        print(" ",end="")
                print("",end=" ")
            print()
xxx()
