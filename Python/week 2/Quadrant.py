"""Quadrant"""
def quadrant():
    """Quadrant"""
    x=int(input())
    y=int(input())
    if not x and not y:
        print("O")
    elif x and not y:
        print("X")
    elif not x and y:
        print("Y")
    elif x>0 and y>0:
        print("Q1")
    elif x < 0 < y:
        print("Q2")
    elif x<0 and y<0:
        print("Q3")
    elif x > 0 > y:
        print("Q4")
quadrant()
