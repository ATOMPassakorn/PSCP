"""Coke"""
def coke():
    """Coke"""
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    if not b:
        price=d*a
    else:
        price=((d//b+1)*c)+((d-(d//b))*a)
    print(price)
coke()
