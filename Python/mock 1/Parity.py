"""Parity"""
def parity():
    """Parity"""
    number=input()
    direct=input()
    bit_1=0
    if direct=="Even":
        for i in number:
            if i=="1":
                bit_1+=1
        if not bit_1%2:
            number+="0"
        else:
            number+="1"
    if direct=="Odd":
        for i in number:
            if i=="1":
                bit_1+=1
        if not bit_1%2:
            number+="1"
        elif bit_1==0:
            number+="0"
        else:
            number+="0"
    print(number)
parity()
