"""Water"""
def water():
    """Water"""
    number=int(input())
    water_price=float(input())
    cube=float(input())
    water_price2=float(input())
    money_pass=float(input())
    ans=0
    price=0
    for _ in range(number):
        use=float(input())
        if use<=cube:
            price=use*water_price
            if price<=money_pass:
                price=0
        elif use>cube:
            price=((use-cube)*water_price2)+(cube*water_price)
            if price<=money_pass:
                price=0
        ans+=price
    print(f"{ans:.2f}")
water()
