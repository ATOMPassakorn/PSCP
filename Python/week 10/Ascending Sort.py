"""ascending_sort"""
def ascending_sort(n):
    """ascending_sort"""
    num_list = []
    for _ in range(n):
        num = int(input())
        num_list.append(num)
    num_list.sort()
    for i in num_list:
        print(i)
ascending_sort(int(input()))
