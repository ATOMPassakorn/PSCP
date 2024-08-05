"""Virus I"""
def virus():
    """Virus I"""
    text=input()
    count=0
    for i in text:
        if i=="o":
            count+=1
    print(count)
virus()
