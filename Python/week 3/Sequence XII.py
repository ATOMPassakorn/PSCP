"""Sequence XII"""
def main():
    """Sequence XII"""
    num=int(input())
    for i in range(-num+1,num):
        for j in range(-num+1,num):
            value = num - abs(abs(i)-abs(j))
            print(f"{value:>02}",end=" ")
        print()
main()
