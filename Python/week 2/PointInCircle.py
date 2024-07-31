"""PointInCircle"""
import math
def circle():
    """PointInCircle"""
    x=int(input())
    y=int(input())
    r=int(input())
    xn=int(input())
    yn=int(input())
    d=math.sqrt(math.pow((xn-x),2)+math.pow((yn-y),2))
    if d <= r:
        print("True")
    else:
        print("False")
circle()
