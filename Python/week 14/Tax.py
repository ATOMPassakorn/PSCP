"""Tax"""
def tax():
    """Tax"""
    year=int(input())
    cc=int(input())
    tax_price=0
    if cc > 1800:
        tax_price+=(cc-1800)*4
        tax_price+=1200*1.5
        tax_price+=600*0.5
    elif cc > 600:
        tax_price+=(cc - 600)*1.5
        tax_price+=600*0.5
    else:
        tax_price+=cc*0.5
    if year==6:
        tax_price*=0.9
    elif year==7:
        tax_price*=0.8
    elif year==8:
        tax_price*=0.7
    elif year==9:
        tax_price*=0.6
    elif year>=10:
        tax_price*=0.5
    print(f"{tax_price:.2f}")
tax()
