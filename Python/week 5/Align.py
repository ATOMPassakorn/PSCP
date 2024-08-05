"""Align"""
import math
def align():
    """Align"""
    size=int(input())
    direc=input()
    text=input()
    if direc=="left":
        print(f"{text:<{size}}")
    elif direc=="right":
        print(f"{text:>{size}}")
    elif direc=="center":
        print(" "*math.ceil((size-len(text))/2),end="")
        print(f"{text}",end="")
        print(" "*math.floor((size-len(text))/2))
align()
