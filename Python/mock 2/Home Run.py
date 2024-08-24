"""Home Run"""
def home():
    """Home Run"""
    num=int(input())
    distance=float(input())
    count=0
    for _ in range(num):
        long=float(input())
        if long<distance:
            count+=1
    print(count)
home()
