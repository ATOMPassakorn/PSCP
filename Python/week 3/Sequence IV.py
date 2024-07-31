"""Sequence IV"""
def main():
    """Sequence IV"""
    num = int(input())
    for i in range(1,num*num+1,num):
        for j in range(i,num+i):
            if j == (num+i):
                print(j, end="")
            else:
                print(j,end=" ")
        print()
main()
