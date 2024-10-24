"""CoinChangev1"""
def coin_greedy():
    """CoinChangev1"""
    num=int(input())
    coins=[25,10,5,1]
    total=0
    for coin in coins:
        total=total+num//coin
        num=num%coin
    print(total)
coin_greedy()
