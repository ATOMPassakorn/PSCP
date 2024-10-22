"""BTU"""
def room1(area):
    """area"""
    start=0
    if 100<=area<151:
        start=5000
    elif 151<=area<251:
        start=6000
    elif 251<=area<301:
        start=7000
    elif 301<=area<351:
        start=8000
    elif 351<=area<401:
        start=9000
    elif 401<=area<451:
        start=10000
    elif 451<=area<551:
        start=12000
    return start

def room2(area):
    """area"""
    start=0
    if 551<=area<701:
        start=14000
    elif 701<=area<1001:
        start=18000
    elif 1001<=area<1201:
        start=21000
    elif 1201<=area<1401:
        start=23000
    elif 1401<=area<1501:
        start=24000
    elif 1501<=area<2001:
        start=30000
    elif 2001<=area<=2500:
        start=34000
    return start

def btu():
    """BTU"""
    area=float(input())
    height=float(input())
    human=float(input())
    room=input()
    sun=input()
    start=0
    if area<551:
        start=room1(area)
        if human>2:
            start+=(human-2)*600
        if height>8:
            start+=(height-8)*1000
        if room=="kitchen":
            start+=4000
        if sun =="shaded":
            start-=start*0.1
        if sun =="facing the sun":
            start+=start*0.1
    else:
        start=room2(area)
        if human>2:
            start+=(human-2)*600
        if height>8:
            start+=(height-8)*1000
        if room=="kitchen":
            start+=4000
        if sun =="shaded":
            start-=start*0.1
        if sun =="facing the sun":
            start+=start*0.1
    print(int(start))
btu()
