"""Alcohol"""
def lspd():
    """Alcohol"""
    sex=input()
    weight=float(input())
    drive=input()
    drink=float(input())
    al_in_drink=float(input())
    can=int(input())
    hour=int(input())
    if sex=="Male":
        man_al=((al_in_drink*drink*can)/100)/(weight*0.68*10)*1000
        if hour>1:
            man_al-=(hour-1)*(15)
        if man_al<50 and drive=="Yes":
            print("Safe")
        elif man_al>=50 or drive=="No":
            print("Not Safe")
    else:
        girl_al=((al_in_drink*drink*can)/100)/(weight*0.55*10)*1000
        if hour>1:
            girl_al-=(hour-1)*(15)
        if girl_al<50 and drive=="Yes":
            print("Safe")
        elif girl_al>=50 or drive=="No":
            print("Not Safe")
lspd()
