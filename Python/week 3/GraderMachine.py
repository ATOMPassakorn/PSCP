"""GraderMachine"""
def counter():
    """GraderMachine"""
    start=int(input())
    stop=int(input())
    som=0
    print("pass :",end=" ")
    if start>stop:
        for i in range(start,stop-1,-1):
            if not i%2:
                print(i,end=" ")
                som+=i
    else:
        for i in range(start,stop+1):
            if not i%2:
                print(i,end=" ")
                som+=i
    print(f"\nSum : {som}")
counter()
