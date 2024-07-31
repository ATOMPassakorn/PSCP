"""Bill"""
def bill():
    """Bill"""
    money=int(input())
    vat10=(money*10)/100
    if vat10<50:
        money+=50
    elif vat10>1000:
        money+=1000
    else:
        money+=vat10
    vat7=money+(money*7/100)
    print(f"{vat7:.2f}")
bill()
