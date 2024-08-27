"""Lift"""
def lift():
    """Lift"""
    num=int(input())
    weigth=float(input())
    total=0
    kids=0
    adult=0
    for _ in range(num):
        age=int(input())
        value=float(input())
        total+=value
        if age<12:
            kids+=1
        else:
            adult+=1
    if (kids and not adult) or total>weigth:
        print("Not Safe")
    else:
        print("Safe")
lift()
