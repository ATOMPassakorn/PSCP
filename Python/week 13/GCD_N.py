"""GCD_N"""
import math as m
def gcd():
    """GCD_N"""
    num_list=[]
    num=int(input())
    for _ in range(num):
        number=int(input())
        num_list.append(number)
    print(m.gcd(*num_list))
gcd()
