"""Niwarn World"""
import math as m
def niwarn(n,s,k):
    """Niwarn World"""
    print(f"X: {x(n):.1f}, Y: {y(n,s):.1f}, Z: {z(k):.1f}")
def x(n):
    """Find x"""
    return 2+(m.log(n**2,2))/(2*n*m.log(n,2))
def y(n,s):
    """Find Y"""
    return (m.sin(m.radians(30))+m.sqrt(2*s))/(x(n)+3)
def z(k):
    """Find Z"""
    return ((y(k,k))**2)+(8456*(x(k))**4)/(24*k)
niwarn(float(input()),float(input()),float(input()))
