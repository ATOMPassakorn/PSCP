"""3nPlus1"""
def plus():
    """3nPlus1"""
    num=int(input())
    while num:
        count=1
        while num!=1:
            if not num%2:
                num/=2
            else:
                num=(num*3)+1
            count+=1
        print(count)
        num=int(input())
plus()
