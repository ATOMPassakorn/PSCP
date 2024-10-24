"""VerticalHistogram"""
import re
def his():
    """VerticalHistogram"""
    text=input()
    vertical=[]
    histogram=[]
    count={}
    clean=re.sub(r"\s*[0-9]*\W*","",text)
    for i in clean:
        vertical.append(i)
    vertical.sort()
    for j in vertical:
        if j not in histogram:
            histogram.append(j)
        count[j]=clean.count(j)
    most=max(count.values())
    for row in range(most, 0, -1):
        if most<10:
            print(f" {most}", end=" ")
            most -= 1
        else:
            print(f"{most}", end=" ")
            most -= 1
        for i in count:
            if row <= count.get(i):
                print(" *", end="")
            else:
                print("  ", end="")
        print()
    print("    ", end="")
    print(*count.keys())
his()
