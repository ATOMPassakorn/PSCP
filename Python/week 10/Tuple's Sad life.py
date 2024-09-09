"""Tuple's Sad life"""
def tuplesad():
    """Tuple's Sad life"""
    number=tuple(map(str,input().split(" ")))
    text=input()
    index=0
    count=number.count(text)
    if count:
        index=number.index(text)
    for _ in range(count):
        for _ in range(count):
            print(index,end=" ")
        print()
tuplesad()
