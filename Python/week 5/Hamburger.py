"""Hamburger"""
def burger():
    """Hamburger"""
    left=int(input())
    right=int(input())
    print("|"*left,end="")
    print("*"*(left+right)*2,end="")
    print("|"*right,end="")
burger()
