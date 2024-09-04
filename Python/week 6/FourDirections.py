"""FourDirections"""
def up_form():
    """up"""
    for i in range(1,6):
        for j in range(1,6):
            if i in (1,4,5) and j==3:
                print("*",end="")
            elif i==2 and j in (2,3,4):
                print("*",end="")
            elif i==3 and j in (1,3,5):
                print("*",end="")
            else:
                print(" ",end="")
        print()
def down_form():
    """down"""
    for i in range(1,6):
        for j in range(1,6):
            if i in (1,2,5) and j==3:
                print("*",end="")
            elif i==3 and j in (1,3,5):
                print("*",end="")
            elif i==4 and j in (2,3,4):
                print("*",end="")
            else:
                print(" ",end="")
        print()
def left_form():
    """left"""
    for i in range(1,6):
        for j in range(1,6):
            if i in (1,5) and j==3:
                print("*",end="")
            elif i==3:
                print("*",end="")
            elif i in (2,4) and j==2:
                print("*",end="")
            else:
                print(" ",end="")
        print()
def right_form():
    """right"""
    for i in range(1,6):
        for j in range(1,6):
            if i in (1,5) and j==3:
                print("*",end="")
            elif i==3:
                print("*",end="")
            elif i in (2,4) and j==4:
                print("*",end="")
            else:
                print(" ",end="")
        print()
def result():
    """Print result"""
    text=input()
    for i in text:
        if i=="U":
            print(up_form(),end=" ")
        elif i=="L":
            print(left_form(),end=" ")
        elif i=="D":
            print(down_form(),end=" ")
        elif i=="R":
            print(right_form(),end=" ")
result()
