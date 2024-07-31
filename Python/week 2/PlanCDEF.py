"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def plan():
    """PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
    side=str(input())
    largest,larger,large=largest_num()
    if side=="Ascend":
        print(f"{large:.2f}, {larger:.2f}, {largest:.2f}")
    elif side=="Descend":
        print(f"{largest:.2f}, {larger:.2f}, {large:.2f}")
def largest_num():
    """Find Num"""
    num1=float(input())
    num2=float(input())
    num3=float(input())
    largest=num1
    larger=num1
    large=num1
    if num2>largest:
        largest=num2
        larger=num1
        if num3>large:
            larger=num3
            large=num1
        else:
            large=num3
    if num3>largest:
        largest=num3
        larger=num1
        if num2>larger:
            larger=num2
            large=num1
        else:
            large=num2
    if largest==num1:
        larger=num2
        if num3>larger:
            larger=num3
            large=num2
        else:
            large=num3
    return largest,larger,large
plan()
