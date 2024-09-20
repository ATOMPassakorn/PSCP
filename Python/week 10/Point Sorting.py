"""Point Sorting"""
def sort_key(point_list):
    """sort"""
    x=int(point_list[0])
    y=int(point_list[1])
    return x+y,-y
def point():
    """Point Sorting"""
    point_list=[]
    number=int(input())
    for _ in range(number):
        num2=int(input())
        for _ in range(num2):
            point_num=input()
            point_list.append(point_num.split())
        point_list=sorted(point_list,key=sort_key)
        for i in point_list:
            print(" ".join(i))
        point_list.clear()
point()
