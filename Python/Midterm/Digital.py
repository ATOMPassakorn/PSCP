"""Digital"""
def digital():
    """Digital"""
    name=input()
    thai=input()
    address=input()
    age=float(input())
    money=float(input())
    widraw=float(input())
    con1=thai in ("Yes","True") and address in ("Yes","True") \
and age>=16 and widraw<=500000 and money<=840000
    if con1:
        print(f"Congratulations! {name} is qualified to receive a digital wallet \
amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
digital()
