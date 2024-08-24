"""Longer"""
import math as m
def longer():
    """Longer"""
    r=float(input())
    a=float(input())
    b=float(input())
    circle=2*m.pi*r
    rec=a*2+b*2
    if rec>circle:
        print("Rectangle is longer")
        print(f"{rec-circle:.5f}")
    elif circle>rec:
        print("Circle is longer")
        print(f"{circle-rec:.5f}")
    else:
        print("Equal")
        print(f"{circle:.5f}")
longer()
