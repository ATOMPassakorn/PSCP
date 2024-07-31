"""BootSequence"""
def main() :
    """BootSequence"""
    num = int(input())
    for i in range(1,num+1) :
        if i==num:
            print(i, end="")
        else:
            print(i, end="_")
main()
