"""3nPlus1"""
def plus():
    """3nPlus1"""
    num=int(input())
    count=0
    while num:
        if not num%2:
            num/=2
            count+=1
        else:
            num=(num*3)+1
            count+=1
        print(count)
plus()
