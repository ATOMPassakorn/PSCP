"""LineSorting"""
def linesort(n):
    """LineSorting"""
    text_list=[]
    for _ in range(n):
        text=input()
        text_list.append(text)
    text_list.sort(key=len)
    for i in text_list:
        print(i)
linesort(int(input()))
