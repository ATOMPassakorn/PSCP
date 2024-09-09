"""Median"""
def med(n):
    """Median"""
    num_list=[]
    median=0
    for _ in range(n):
        number=float(input())
        num_list.append(number)
        num_list.sort()
    if not len(num_list)%2:
        median=(num_list[int(len(num_list)/2)-1]+num_list[int((len(num_list)/2))])/2
    else:
        median=num_list[int(len(num_list)/2)]
    print(f'{median:.3f}')
med(int(input()))
