"""Diginity"""
def dignity():
    """Diginity"""
    num=input()
    while num!="0":
        if len(num)>=2:
            total=0
            while len(num)> 1:
                total=0
                for i in num:
                    total+=int(i)
                num=str(total)
        print(num)
        num=input()
dignity()
