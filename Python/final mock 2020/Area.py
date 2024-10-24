"""Area"""
def area():
    """Area"""
    number=int(input())
    total=0
    for _ in range(number):
        picture=input().strip()
        clean=picture.replace(" ","")
        total+=len(clean)
    print(total)
area()
