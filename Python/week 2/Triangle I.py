"""Triangle I"""
def pythagoras():
    """Triangle I"""
    a=float(input())
    b=float(input())
    c=float(input())
    tri1=abs(c**2-(a**2+b**2))
    tri2=abs(a**2-(c**2+b**2))
    tri3=abs(b**2-(a**2+c**2))
    if tri1<=0.01 or tri2<=0.01 or tri3<=0.01:
        print("Yes")
    else:
        print("No")
pythagoras()
