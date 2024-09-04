"""FourDirections"""
def up_form(row):
    """up"""
    result = ""
    for j in range(1,6):
        if row in (1,4,5) and j==3:
            result+="*"
        elif row==2 and j in (2,3,4):
            result+="*"
        elif row==3 and j in (1,3,5):
            result+="*"
        else:
            result+=" "
    return result
def down_form(row):
    """down"""
    result = ""
    for j in range(1,6):
        if row in (1,2,5) and j==3:
            result+="*"
        elif row==3 and j in (1,3,5):
            result+="*"
        elif row==4 and j in (2,3,4):
            result+="*"
        else:
            result+=" "
    return result
def left_form(row):
    """left"""
    result = ""
    for j in range(1,6):
        if row in (1,5) and j==3:
            result+="*"
        elif row==3:
            result+="*"
        elif row in (2,4) and j==2:
            result+="*"
        else:
            result+=" "
    return result
def right_form(row):
    """right"""
    result = ""
    for j in range(1,6):
        if row in (1,5) and j==3:
            result+="*"
        elif row==3:
            result+="*"
        elif row in (2,4) and j==4:
            result+="*"
        else:
            result+=" "
    return result
def answer():
    """Print result"""
    text=input()
    for row in range(1, 6):
        ans=""
        for i in text:
            if i=="U":
                ans+=up_form(row)+" "
            elif i=="L":
                ans+=left_form(row)+" "
            elif i=="D":
                ans+=down_form(row)+" "
            elif i=="R":
                ans+=right_form(row)+" "
        print(ans)
answer()
