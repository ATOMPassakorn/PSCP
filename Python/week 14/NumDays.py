"""NumDays"""
import datetime
def demons():
    """NumDays"""
    try:
        first_day=int(input())
        first_month=int(input())
        second_day=int(input())
        second_month=int(input())
        first_date=datetime.date(2017,first_month,first_day)
        second_date=datetime.date(2017,second_month,second_day)
        difference=second_date-first_date
        print(difference.days)
    except ValueError:
        print("Impossible")
demons()
