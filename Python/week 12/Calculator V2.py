"""Calculator V2"""
def cal():
    """Calculator V2"""
    num=int(input())
    total=0
    length=len(str(num))
    for i in range(1,length):
        total+=i*(9*10**(i-1))+(9*10**(i-1))
    total+=length*(num-10**(length-1)+1)+(num-10**(length-1)+1)
    if num==1:
        total=1
    print(total)
cal()
