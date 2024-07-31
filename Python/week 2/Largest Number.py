"""Largest Number"""
def number():
    """Largest Number"""
    num1=input()
    num2=input()
    num3=input()
    a=int(num1+num2+num3)
    b=int(num1+num3+num2)
    c=int(num2+num1+num3)
    d=int(num2+num3+num1)
    e=int(num3+num1+num2)
    f=int(num3+num2+num1)
    largest=a
    if b>largest:
        largest=b
    if c>largest:
        largest=c
    if d>largest:
        largest=d
    if e>largest:
        largest=e
    if f>largest:
        largest=f
    print(largest)
number()
