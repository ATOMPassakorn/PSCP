"""BreachTheDoor"""
def door():
    """BreachTheDoor"""
    text=input()
    text_sum=""
    for i in text:
        if i.isalpha() or i.isspace():
            text_sum+=i
    text_list=text_sum.split()
    for j in text_list:
        if len(j)>6:
            print(j,end=" ")
door()
