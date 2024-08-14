"""Pringles"""
def potato():
    """Pringles"""
    up=input()
    middle=input()
    low=input()
    number=int(input())
    count=0
    new_mid=""
    old=middle
    for _ in range(number):
        new_mid+=middle[0]
        middle=middle[1:]
    for i in new_mid:
        if i == ")":
            count+=1
    print(count)
    if not ")" in middle:
        print("None.")
    else:
        print("There are still some left.")
    print(up)
    if count>0:
        print((" "*number)+middle)
    else:
        print(old)
    print(low)
potato()
