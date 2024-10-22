"""PH"""
def ph():
    """PH"""
    number=float(input())
    if 0<=number<7:
        print("acidic")
    elif number==7:
        print("neutral")
    elif 7<=number<=14:
        print("akaline")
    else:
        print("error")
ph()
