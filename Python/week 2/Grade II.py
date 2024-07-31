"""Grade II"""
def main():
    """Grade II"""
    point = float(input())
    if 100 < point or point < 0:
        print("ERR")
    elif 100 >= point >= 95:
        print("A")
    elif 95 > point >= 90:
        print("B+")
    elif 90 > point >= 85:
        print("B")
    elif 85 > point >=80:
        print("C+")
    elif 80 > point >= 75:
        print("C")
    elif 75 > point >= 70:
        print("D+")
    elif 70 > point >= 65:
        print("D")
    elif 65 > point >= 60:
        print("F+")
    elif 60 > point >= 0:
        print("F")
main()
