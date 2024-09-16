"""MissingNumber No Set"""
def missing():
    """MissingNumber No Set"""
    stop=int(input())
    check_list=[]
    num_list=[]
    for i in range(1,stop+1):
        check_list.append(i)
    number=float('inf')
    while number:
        number=int(input())
        num_list.append(number)
    for i in check_list:
        if i not in num_list:
            print(i)
missing()
