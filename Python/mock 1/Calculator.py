"""Calculator"""
def cal():
    """Calculator"""
    n=int(input())
    total=0
    for i in range(1,n+1):
        i=len(str(i))
        total+=i+1
    if n==1:
        total=1
    print(total)
cal()
