"""Stamps"""
import math as m
def stamp():
    """Stamps"""
    rounds=int(input())
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    stamps=0
    money=0
    for _ in range(rounds):
        price=int(input())
        discount=0
        if stamps>=c:
            pro=(stamps//c)*d
            if price>=pro:
                use=(stamps//c)*c
            else:
                use=m.ceil(price/d)*c
            discount+=(use//c)*d
            stamps-=use
        price=max(0,price-discount)
        if price>=a:
            stamps+=(price//a)*b
        money+=price
    print(money)
    print(stamps)
stamp()
