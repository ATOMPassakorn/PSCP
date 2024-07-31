"""MyMath"""
import math
def main():
    """MyMath"""
    x = (math.sin(math.radians(90))+math.pow(math.sin(math.radians(60)),2)) \
    / (math.cos(math.radians(math.pow(245,2))) \
    +(math.cos(math.radians(45+135))))
    y = (math.factorial(16)*math.factorial(4))/(math.factorial(8))
    z = (15+25)/math.sqrt(math.pow(25-12,2)+math.pow(12-15,2))
    a = math.log10(math.pow(1234,4))
    b = (math.log(4234,5)+math.log(8191,2)+71*math.log(156154,10))\
    /(math.log(777,7)-math.log(888,8)-math.log(999,9))
    print(x)
    print(y)
    print(z)
    print(a)
    print(b)
main()
