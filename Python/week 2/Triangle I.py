"""Triangle I"""
def pythagoras():
    """Triangle I"""
    a=float(input())
    b=float(input())
    c=float(input())
    tri1=abs((a+b)-c)
    tri2=abs((a+c)-b)
    tri3=abs((b+c)-a)
    tri4=abs(c**2-(a**2+b**2))
    if tri1<=0.01 or tri2<=0.01 or tri3<=0.01 or tri4<=0.01:
        print("Yes")
    else:
        print("No")
pythagoras()
