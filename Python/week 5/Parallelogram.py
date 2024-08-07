"""Parallelogram"""
def italy():
    """Parallelogram"""
    text=input()
    num = len(text)
    space=num-1
    index=1
    for i in range(0,num):
        print(" "*space+text[:index],end="")
        index+=1
        space-=1
        print()
    for i in range(num,1,-1):
        for j in range(i-1,0,-1):
            print(text[num-j],end="")
        print()
italy()
