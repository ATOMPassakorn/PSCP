"""Inflation"""
def inflation():
    """Inflation"""
    number=int(float(input())*100)
    kumber=int(input())
    inflation_rate=381
    for _ in range(kumber):
        number+=(number*inflation_rate)//10000
    print(f"{number//100}.{number%100:02d}")
inflation()
