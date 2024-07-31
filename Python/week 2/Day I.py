"""Day I"""
def day():
    """Day I"""
    num=int(input())
    if not num%4:
        if num%100:
            print("Yes")
        else:
            if num%400:
                print("No")
            else:
                print("Yes")
    else:
        print("No")
day()
