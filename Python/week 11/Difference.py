"""Difference"""
def difference():
    """Difference"""
    a=int(input())
    b=int(input())
    set_a=set()
    set_b=set()
    for _ in range(a):
        num_a=int(input())
        set_a.add(num_a)
    for _ in range(b):
        num_b=int(input())
        set_b.add(num_b)
    diff=sorted(set_a.difference(set_b))
    for i in diff:
        print(i,end=" ")
difference()
