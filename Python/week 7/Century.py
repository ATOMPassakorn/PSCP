"""Century"""
import math as m
def century():
    """Century"""
    num=int(input())
    for _ in range(num):
        year=input()
        cen=year[0:5]
        this_year=int(year[5::])
        if cen == "B.E. ":
            this_year-=543
            if this_year<=0:
                print("ERROR")
            else:
                print(m.ceil(this_year/100))
        elif cen == "A.D. ":
            print(m.ceil(this_year/100))
        else:
            print("ERROR")
century()
