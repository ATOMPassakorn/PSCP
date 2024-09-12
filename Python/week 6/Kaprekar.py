"""Kaprekar"""
def kaprekar():
    """Kaprekar"""
    number=input()
    return number
def most(number):
    """find most"""
    num1=""
    for _ in range(4):
        maz="0"
        for i in number:
            if i>maz:
                maz=i
        num1+=maz
        number = number.replace(maz, '', 1)
    return num1
def least(number):
    """find least"""
    num2=""
    for _ in range(4):
        miz="9"
        for i in number:
            if i<miz:
                miz=i
        num2+=miz
        number = number.replace(miz, '', 1)
    return num2
def find(number):
    """find kaprekar"""
    count=0
    result=0
    number=f"{int(number):04}"
    while result!=6174:
        mostnum=most(number)
        leastnum=least(number)
        result=int(mostnum)-int(leastnum)
        count+=1
        number = f"{result:04}"
    print(count)
ans=kaprekar()
find(ans)
