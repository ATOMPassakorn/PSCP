"""coffee shop"""
def coffee():
    """coffee"""
    a=float(input())
    b=float(input())
    c=float(input())
    d=float(input())
    e=int(input())
    price_1=(1*a)+(((e-1)*a)-(e-1)*(a*(b/100)))
    price_2=e*a
    if price_2>=d:
        price_2=e*a-((e*a)*c/100)
    if price_1<price_2:
        print("1")
        print(f"{price_1:.2f}")
    elif price_2<price_1:
        print("2")
        print(f"{price_2:.2f}")
    else:
        print("2")
        print(f"{price_2:.2f}")
coffee()
