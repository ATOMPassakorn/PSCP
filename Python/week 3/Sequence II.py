"""Sequence II"""
def main():
    """Sequence II"""
    num = int(input())
    for i in range(1,num+1):
        if i == num:
            print(i**2,end="")
        else:
            print(i**2,end=" ")
main()
