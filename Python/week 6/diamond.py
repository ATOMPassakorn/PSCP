"""diamond"""
def diamond():
    """diamond"""
    num=int(input())
    size=int((num/2)+1)
    for i in range(size):
        if i==size-1:
            print("*"*num)
            break
        for j in range(1,num+1):
            if j in (size-i,size+i):
                print("*",end="")
            else:
                print(" ",end="")
        print()
    for i in range(size-2,-1,-1):
        for j in range(1,num+1):
            if j in (size-i, size+i):
                print("*",end="")
            else:
                print(" ",end="")
        print()
diamond()
