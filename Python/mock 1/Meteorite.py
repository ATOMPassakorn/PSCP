"""Meteorite"""
def meteorite():
    """Meteorite"""
    a=float(input())
    b=int(input())
    c=float(input())
    shoot=1
    for _ in range(b):
        now_meteor=a/b
        while now_meteor>c:
            shoot+=1
            now_meteor=now_meteor/b
    print(shoot)
meteorite()
