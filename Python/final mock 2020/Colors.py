"""Colors"""
def colors():
    """Colors"""
    color1=input()
    color2=input()
    violet=["Red","Blue"]
    orange=["Red","Yellow"]
    green=["Yellow","Blue"]
    if color1==color2 and color1 in ("Red","Blue","Yellow") and color2 in ("Red","Blue","Yellow"):
        print(color1)
        return
    if color1 in violet and color2 in violet:
        print("Violet")
    elif color1 in orange and color2 in orange:
        print("Orange")
    elif color1 in green and color2 in green:
        print("Green")
    else:
        print("Error")
colors()
