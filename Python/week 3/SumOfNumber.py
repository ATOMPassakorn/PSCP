"""SumOfNumber"""
def number():
    """SumOfNumber"""
    i=int(input())
    som=0
    target=i
    while i!=-1 and som!=target:
        i=int(input())
        if i==-1:
            som+=1
        som+=i
    print(som)
number()
