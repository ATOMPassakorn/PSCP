"""Sequence VI"""
def main():
    """Sequence VI"""
    num = int(input())
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i>=j:
                print(j,end=" ")
        print()
main()
