"""Circular II"""
import math
def circular():
    """Circular II"""
    X=float(input())
    Y=float(input())
    r1=float(input())
    x=float(input())
    y=float(input())
    r2=float(input())
    d=math.sqrt(math.pow((x-X),2)+math.pow((y-Y),2))
    if d < r1+r2:
        print("Yes")
    else:
        print("No")
circular()
