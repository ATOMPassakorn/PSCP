"""Password"""
import math as m
def password():
    """Password"""
    text=input()
    special='''~`!@#$%&^*()-_+={ }[\\]|/:;'"<>,.?'''
    r=0
    lower=False
    upper=False
    digit=False
    spec=False
    for i in text:
        if i.islower():
            lower=True
        elif i.isupper():
            upper=True
        elif i.isdigit():
            digit=True
        elif i in special:
            spec=True
    if lower:
        r+=26
    if upper:
        r+=26
    if digit:
        r+=10
    if spec:
        r+=32
    entropy=int(m.log2(r**len(text)))
    return entropy
def strength():
    """Passaword Strength"""
    entropy=password()
    print(entropy)
    if entropy < 28 :
        print("Very Weak")
    elif 28 <= entropy < 36:
        print("Weak")
    elif 36 <= entropy < 60:
        print("Reasonable")
    elif 60 <= entropy < 127:
        print("Strong")
    else:
        print("Very Strong")
strength()
