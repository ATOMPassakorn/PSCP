"""Dart"""
import math as m
def dart():
    """Dart"""
    num=int(input())
    total=0
    for _ in range(num):
        score=input()
        x,y=score.split()
        x,y=int(x),int(y)
        distance = m.sqrt(m.pow(x,2)+m.pow(y,2))
        if distance <= 2:
            total+=5
        elif distance <= 4:
            total+=4
        elif distance <= 6:
            total+=3
        elif distance <= 8:
            total+=2
        elif distance <= 10:
            total+=1
    print(total)
dart()
