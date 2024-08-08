"""Donut"""
def donut():
    """Donut"""
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    box_set=d//(b+c)
    price=box_set*b*a
    buy=(b+c)*box_set
    if buy < d:
        buy+=b+c
        price+=b*a
    print(f"{price} {buy}")
donut()
