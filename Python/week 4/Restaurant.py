"""Restaurant"""
def res():
    """Restaurant"""
    a=float(input())
    b=float(input())
    c=float(input())
    d=float(input())
    price_1=(a+d)-((a+d)*c)/100
    price_2=a-(a*c)/100
    if a==b:
        if a == b and not d:
            print("Yes")
        elif price_2==price_1:
            print("Yes")
        elif price_2<price_1:
            print(f"No {price_1-price_2:.3f}")
    elif a+d>=b:
        if price_1==a:
            print("Yes")
        elif price_1==price_2:
            print("Yes")
        elif price_1>a:
            print(f"No {price_1-a:.3f}")
        else:
            print(f"Yes {a-price_1:.3f}")
    else:
        print("Yes")
res()
