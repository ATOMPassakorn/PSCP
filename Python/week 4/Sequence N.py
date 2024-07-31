"""Sequence N"""
def nword():
    """Sequence N"""
    num=int(input())
    for i in range(1,num+1):
        for j in range(1,num+1):
            if  j in (num,i,1):
                print("*",end="")
            else:
                print(" ",end="")
        print()
nword()
