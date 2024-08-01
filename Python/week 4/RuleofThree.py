"""RuleofThree"""
def rule():
    """RuleofThree"""
    num=int(input())
    best_price=0
    best_weight=0
    value=0
    for _ in range(num):
        price=float(input())
        weight=float(input())
        if weight/price>value:
            best_price=price
            best_weight=weight
            value=weight/price
        elif weight/price==value:
            best_price=min(price)
            best_weight=min(weight)
    print(f"{best_price:.2f} {best_weight:.2f}")
rule()
