"""Milk"""
def milk():
    """Milk"""
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    buy=d//a
    cap=buy
    while cap>=b and b:
        milk_add=(cap//b)*c
        buy+=milk_add
        cap=(cap%b)+milk_add
    print(buy)
milk()
