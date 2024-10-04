"""Sort"""
def selection():
    """Sort"""
    num=""
    arr=[]
    while num!="END":
        num=input()
        if num=="END":
            break
        arr.append(int(num))
    lenght=len(arr)
    for i in range(lenght):
        min_num=i
        for j in range(i+1,lenght):
            if arr[j]<arr[min_num]:
                min_num=j
        arr[i], arr[min_num] = arr[min_num], arr[i]
    for i in arr:
        print(i)
selection()
