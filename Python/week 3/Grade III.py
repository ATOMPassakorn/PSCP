"""Grade III"""
import math
def main():
    """Grade III"""
    num=int(input())
    count=0
    grade=0
    while count<num:
        point = float(input())
        if 100 >= point >= 95:
            grade+=4
            count+=1
        elif 95 > point >= 90:
            grade+=3.5
            count+=1
        elif 90 > point >= 85:
            grade+=3
            count+=1
        elif 85 > point >=80:
            grade+=2.5
            count+=1
        elif 80 > point >= 75:
            grade+=2
            count+=1
        elif 75 > point >= 70:
            grade+=1.5
            count+=1
        elif 70 > point >= 65:
            grade+=1
            count+=1
        elif 65 > point >= 60:
            grade+=0.5
            count+=1
        elif 60 > point >= 0:
            count+=1
    ans=grade/num
    grade=math.floor(ans*100)/100
    print(f"{grade:.2f}")
main()
