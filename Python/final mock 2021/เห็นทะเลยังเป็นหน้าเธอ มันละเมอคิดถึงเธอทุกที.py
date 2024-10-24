"""เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
def shark():
    """เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
    fish=input()
    shallow=["BULL SHARK"]
    twilight=["CHAIN CATSHARK","GREAT WHITE SHARK","GUMMY SHARK","BLUE SHARK","MAKO SHARK"]
    midnight=["FRILLED SHARK","GOBLIN SHARK","SIXGILL SHARK","GREENLAND SHARK","COOKIECUTTER SHARK"]
    abyssal=["MEGAMOUTH SHARK"]
    if fish in shallow:
        print("THE SHALLOW ZONE")
    elif fish in twilight:
        print("THE TWILIGHT ZONE")
    elif fish in midnight:
        print("THE MIDNIGHT ZONE")
    elif fish in abyssal:
        print("THE ABYSSAL ZONE")
    else:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
shark()
