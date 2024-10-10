"""Book Worm"""
def book():
    """Book Worm"""
    test_num=int(input())
    for _ in range(test_num):
        count=0
        time=0
        book_read=float(input())
        book_num=int(input())
        data=[]
        for _ in range(book_num):
            book_time=float(input())
            data.append(book_time)
            data.sort()
        for i in data:
            if time+i<=book_read:
                time+=i
                count+=1
        print(count)
book()
