"""Books"""
import math as m
def book():
    """Books"""
    num_book=int(input())
    page=int(input())
    x=int(input())
    y=int(input())
    day=0
    left=num_book
    for _ in range(num_book):
        page_read=0
        while page_read<page:
            read=m.ceil(((x+day)/(y+day))*page)
            if read>=page:
                day+=left
                left=0
                break
            page_read+=read
            day+=1
        if not left:
            break
        left-=1
    print(day)
book()
