"""Christmas"""
def tree():
    """Christmas"""
    num=int(input())
    k=int(input())
    for i in range(0,num):
        for _ in range(0,num-i-1):
            print(" ",end="")
        for _ in range(0,2*i+1):
            print("*",end="")
        print()
    for i in range(0,k):
        print(" "*(num-2)+"-"*3)
tree()
