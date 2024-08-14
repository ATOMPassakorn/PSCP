"""Harshad"""
def harshard():
    """Harshad"""
    for _ in range(10):
        number=input()
        old=int(number)
        total=0
        for i in number:
            if i.isnumeric():
                total+=int(i)
        new=total
        if not new or not old:
            print("No")
        elif not old % new:
            print("Yes")
        else:
            print("No")
harshard()
