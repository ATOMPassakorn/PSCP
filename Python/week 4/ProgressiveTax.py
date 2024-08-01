"""ProgressiveTax"""
def tax():
    """ProgressiveTax"""
    money=int(input())
    if 0 < money <= 150000:
        print(0)
    elif 150000 < money <= 300000:
        print(int((money-150000)*(5/100)))
    elif 300000 < money <= 500000:
        print(int((money-300000)*(10/100)+7500))
    elif 500000 < money <= 750000:
        print(int((money-500000)*(15/100)+27500))
    elif 750000 < money <= 1000000:
        print(int((money-750000)*(20/100)+65000))
    elif 1000000 < money <= 2000000:
        print(int((money-1000000)*(25/100)+115000))
    elif 2000000 < money <= 4000000:
        print(int((money-2000000)*(30/100)+365000))
    else:
        print(int((money-4000000)*(35/100)+965000))
tax()
