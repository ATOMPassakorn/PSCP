"""Ping"""
import math as m
def ping():
    """Ping"""
    input()
    input()
    line3=input()
    if "[" in line3:
        start=line3.index("[")+1
        stop=line3.index("]")
        ip=line3[start:stop]
    else:
        ip=line3[8:-23]
    received=4
    lost=0
    avg=0
    minus=m.inf*-1
    plus=m.inf
    for _ in range(4):
        line4_7=input()
        if "Reply" in line4_7:
            start=line4_7.index("time")+5
            stop=line4_7.index("ms")
            logic=line4_7[line4_7.index("time")+4]
            if logic=="<":
                speed=0
            else:
                speed=int(line4_7[start:stop])
            avg+=speed
            minus=max(speed,minus)
            plus=min(speed,plus)
        else:
            received-=1
            lost+=1
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = {received}, Lost = {lost} ({lost/4*100:.0f}% loss),")
    if received>0:
        avg=avg//received
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {plus}ms, Maximum = {minus}ms, Average = {avg}ms")
ping()
