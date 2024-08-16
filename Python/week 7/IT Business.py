"""IT Business"""
def business():
    """IT Business"""
    start_money=float(input())
    money_now=float(input())
    atm=""
    fail=0
    while atm!="end":
        atm=input()
        if atm[0]=="D" and float(atm[2:])<=money_now:
            money_now-=float(atm[2:])
            start_money+=float(atm[2:])
            fail=0
        elif atm[0]=="W" and float(atm[2:])<=start_money:
            start_money-=float(atm[2:])
            money_now+=float(atm[2:])
            fail=0
        else:
            fail+=1
        if fail==3:
            break
    print(f"{start_money:.2f}")
    print(f"{money_now:.2f}")
business()
