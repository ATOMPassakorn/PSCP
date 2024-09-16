"""Amefuri Plus"""
def amefuri():
    """Amefuri Plus"""
    hour=int(input())
    log=input().lower()
    humid=8
    lost=False
    for i in log:
        if humid <= 0:
            break
        if 6 <= hour < 18:
            humid,lost = day(i,humid,lost)
        elif 0<=hour<6 or 18<=hour<=24:
            humid,lost = night(i,humid,lost)
        hour=(hour+1)%24
    if lost:
        print("Lost")
    elif humid<=0:
        print("Dry")
    else:
        print(f"Still Wet (Wet Level: {humid:.2f})")
def day(weather,humid,lost):
    """day"""
    if humid>16:
        humid=16
    if weather=="c":
        humid-=0.5
    elif weather=="n":
        humid-=1
    elif weather=="w":
        humid-=1.5
    elif weather=="r":
        humid+=2
    elif weather=="s":
        humid+=3
    elif weather=="h":
        lost=True
    return humid,lost
def night(weather,humid,lost):
    """night"""
    if humid>16:
        humid=16
    if weather=="c":
        humid-=0.25
    elif weather=="n":
        humid-=0.5
    elif weather=="w":
        humid-=0.75
    elif weather=="r":
        humid+=2
    elif weather=="s":
        humid+=3
    elif weather=="h":
        lost=True
    return humid,lost
amefuri()
