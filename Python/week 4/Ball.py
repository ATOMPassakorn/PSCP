"""Ball"""
def ball():
    """Ball"""
    high=float(input())
    count=0
    high=high*3/5
    while high>0.01:
        count+=1
        high=high*3/5
    print(count)
ball()
