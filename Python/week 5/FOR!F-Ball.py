"""FOR!F-Ball"""
def ball():
    """FOR!F-Ball"""
    text=input()
    rotate=1
    for i in text:
        if i =="A":
            if rotate==1:
                rotate=2
            elif rotate==2:
                rotate=1
        elif i == "B":
            if rotate==2:
                rotate=3
            elif rotate==3:
                rotate=2
        elif i == "C":
            if rotate==1:
                rotate=3
            elif rotate==3:
                rotate=1
    print(rotate)
ball()
