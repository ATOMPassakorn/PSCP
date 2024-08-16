"""Century"""
def century():
    """Century"""
    num=int(input())
    for _ in range(num):
        year=input()
        cen=year[0:4]
        this_year=int(year[4::])
        if cen == "B.E.":
            this_year-=543
        elif cen== "A.D.":
            this_year+=0
        else:
            print("ERROR")
        if not this_year%100:
            this_year=this_year//100
        else:
            this_year=(this_year//100)+1
        print(this_year)
century()
