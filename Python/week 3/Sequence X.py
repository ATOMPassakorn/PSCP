"""Sequence X"""
def main():
    """Sequence X"""
    num=int(input())
    for i in range(1,num+1):
        print("   "*(num-i),end="")
        for j in range(1,i):
            print(f"{j:02}",end=" ")
        for i in range(i,0,-1):
            print(f"{i:02}",end=" ")
        print()
    for i in range(num-1,0,-1):
        print("   "*(num-i),end="")
        for j in range(1,i):
            print(f"{j:02}",end=" ")
        for i in range(i,0,-1):
            print(f"{i:02}",end=" ")
        print()
main()
