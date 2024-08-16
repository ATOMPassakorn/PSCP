"""Cha Cha Cha"""
import math
def cha(n):
    """Cha Cha Cha"""
    hours = 0
    for _ in range(n):
        hours += math.ceil(float(input()))
    print(hours*8720)
cha(int(input()))
