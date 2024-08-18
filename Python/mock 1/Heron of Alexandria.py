"""Heron of Alexandria"""
import math as m
def tri():
    """Heron of Alexandria"""
    a=float(input())
    b=float(input())
    c=float(input())
    s=(a+b+c)/2
    area=m.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"{area:.3f}")
tri()
