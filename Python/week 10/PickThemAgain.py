"""pickthemagain"""
def pickthemagain(text):
    """pickthemagain"""
    num_list = text.split()
    num_list = num_list[::-1]
    count = 0
    for i in num_list:
        if not int(i)%3 or not int(i)%5:
            count += 1
            print(i)
    if not count:
        print("Nope")
pickthemagain(input())
