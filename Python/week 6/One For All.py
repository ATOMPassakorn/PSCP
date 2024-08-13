"""One For All"""
def bestmanga():
    """One For All"""
    num=int(input())
    count=1
    even=2
    odd=1
    hero=""
    for i in range(num):
        ofa=input()
        if count%2 and count!=num:
            hero+=(ofa+"*"*odd)
            odd+=2
        elif not count%2 and count!=num:
            hero+=(ofa+"-"*even)
            even+=2
        count+=1
        if i==num-1:
            hero+=(f"{ofa}_{num}")
    print(hero)
bestmanga()
