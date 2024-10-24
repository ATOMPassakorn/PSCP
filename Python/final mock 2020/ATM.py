"""ATM"""
def atm():
    """ATM"""
    money=int(input())
    bank=""
    while bank!="END":
        bank=input().split(" ")
        if bank[0]=="END":
            break
        deal=bank[0]
        eco=int(bank[1])
        if deal=="D":
            money+=eco
        elif deal=="W":
            money-=eco
            if money<0:
                money=0
    print(money)
atm()
