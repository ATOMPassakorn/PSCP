"""Meteorite"""
def meteorite():
    """Meteorite"""
    a=float(input())
    b=int(input())
    c=float(input())
    shoot=0
    meteor=1
    while a>=c:
        shoot+=meteor
        meteor*=b
        a/=b
    print(shoot)
meteorite()
