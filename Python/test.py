"""books"""
import math
def main():
    """printing process of the program"""
    def day_cnt(book_amount, pages, x, y): #read (x/y) pages
        """find amount of days Harry gonna read"""
        read_page = 0
        day = 0
        book_left = book_amount
        for _ in range(1, book_amount+1):
            read_page = 0
            while read_page < pages:
                readable = math.ceil((x/y) * pages)
                if readable >= pages: #จบแต่ละวันได้เลย ไม่จำเป็นต้องคำนวณด้านล่าง
                    day += book_left
                    return day
                read_page += readable
                x += 1
                y += 1
                day += 1
            book_left -= 1
        return day
    print(day_cnt(int(input()), int(input()), int(input()), int(input())))
main()
# import math
# n = 300000
# k = 50
# x = 1
# y = 5
# for num in range(0, 1000):
#     print(f"{x+num}/{y+num} = {math.ceil((x+num)/(y+num)*k)}")