"""Duplicate I"""
def dup():
    """Duplicate I"""
    m = int(input())
    n = int(input())

    group_1 =""
    group_2 =""

    for _ in range(m):
        student_id = input().strip()
        group_1 += student_id + " "

    for _ in range(n):
        student_id = input().strip()
        if student_id in group_1:
            group_2 += student_id + " "

    group_2 = group_2.strip().split()
    if group_2:
        for student_id in sorted(group_2,reverse=True):
            print(student_id)
    else:
        print("Nope")
dup()
