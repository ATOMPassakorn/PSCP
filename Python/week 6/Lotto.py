"""Lotto"""
def lotto():
    """Lotto"""
    first=input()
    sec=input()
    third1=input()
    third2=input()
    third3=input()
    third4=input()
    number=input()
    total=0
    near_1=f"{int(first)-1:06}"
    near_2=f"{int(first)+1:06}"
    if number==first:
        total+=6_000_000
    if number[-2:]==sec:
        total+=2_000
    if number[:3] == third1:
        total+=4_000
    if number[:3] == third2:
        total+=4_000
    if number[-3:] == third3:
        total+=4_000
    if number[-3:] == third4:
        total+=4_000
    if first == "000000":
        near_1 = "999999"
        near_2 = "000001"
    elif first == "999999":
        near_1 = "999998"
        near_2 = "000000"
    if number in (near_1 ,near_2):
        total+=100_000
    print(total)
lotto()
