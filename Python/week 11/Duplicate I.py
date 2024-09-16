"""Duplicate I"""
def duplicate():
    """Duplicate I"""
    m = int(input())
    n = int(input())
    first_set=set()
    seconds_set=set()
    for _ in range(m):
        student=int(input())
        first_set.add(student)
    for _ in range(n):
        student=int(input())
        seconds_set.add(student)
    intersect=sorted(first_set.intersection(seconds_set),reverse=True)
    if intersect:
        for i in intersect:
            print(i)
    else:
        print("Nope")
duplicate()
