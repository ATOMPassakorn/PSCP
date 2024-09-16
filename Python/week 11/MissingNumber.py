"""MissingNumber"""
def missing():
    """MissingNumber"""
    stop=int(input())
    check_set=set()
    num_set=set()
    for i in range(1,stop+1):
        check_set.add(i)
    number=float('inf')
    while number:
        number=int(input())
        num_set.add(number)
    diff=check_set.difference(sorted(num_set))
    for i in diff:
        print(i)
missing()
