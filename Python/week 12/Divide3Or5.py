"""Divide3Or5"""
def threeorfive():
    """Divide3Or5"""
    num=int(input())
    num_list=[]
    for i in range(1,num+1):
        if not i%3 or not i%5:
            num_list.append(i)
    print(sum(num_list))
threeorfive()
