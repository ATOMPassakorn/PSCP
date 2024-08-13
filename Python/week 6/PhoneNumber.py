"""PhoneNumber"""
def phone():
    """PhoneNumber"""
    number=input()
    country=input()
    first=""
    seconds=""
    third=""
    if country=="Domestic" and len(number)==9:
        first=number[0]
        seconds=number[1:5]
        third=number[5:]
    elif country=="Domestic":
        first=number[0:2]
        seconds=number[2:6]
        third=number[6:]
    elif country=="International" and len(number)==9:
        first="+66"
        seconds=number[1:5]
        third=number[5:]
    elif country=="International":
        first="+66"+number[1]
        seconds=number[2:6]
        third=number[6:]
    print(f"{first} {seconds} {third}")
phone()
