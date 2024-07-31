"""Sequence III"""
def main():
    """Sequence III"""
    num = int(input())
    for i in range(1,num+1):
        for j in range(i+1,num+i+1):
            if j == (num+i):
                print(j, end="")
            else:
                print(j,end=" ")
        print()
main()
