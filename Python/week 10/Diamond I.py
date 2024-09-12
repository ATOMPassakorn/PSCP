"""Diamond I"""
def diamond_1():
    """Diamond I"""
    m=int(input())
    n=int(input())
    list_1=[]
    column_list=[]
    for _ in range(m):
        number=input()
        list_1.append(number.split(" "))
    for i in range(n):
        column_sum = 0
        for row in list_1:
            column_sum += int(row[i])
        column_list.append(column_sum)
    print(max(column_list))
diamond_1()
