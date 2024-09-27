"""Coke V2"""
import math as m
def coke():
    """Coke V2"""
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    if not b:
        price=d*a
    elif not d:
        price=0
    else:
        price=((a*d)-(m.ceil((d-b)/b)*(a-c)))
    print(price)
coke()
