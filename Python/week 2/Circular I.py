"""Circular I"""
import math
def circular():
    """Circular I"""
    X=float(input())
    Y=float(input())
    r=float(input())
    x=float(input())
    y=float(input())
    d=math.sqrt(math.pow((x-X),2)+math.pow((y-Y),2))
    if d <= r:
        print("Yes")
    else:
        print("No")
circular()
