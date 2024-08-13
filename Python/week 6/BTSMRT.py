"""BTSMRT"""
def train():
    """BTSMRT"""
    day=input()
    age=float(input())
    height=float(input())
    if age<14 and height<90:
        print("FREE")
    elif day=="Children Day" and age<14 and height<=140:
        print("FREE")
    elif day=="Senior Day" and age>=60:
        print("FREE")
    else:
        print("PAY")
train()
