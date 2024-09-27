"""Day2011"""
def day2011():
    """Day2011"""
    day=int(input())
    month=int(input())
    year=2011
    if month in (1,2):
        month+=12
        year-=1
    k=year%100
    j=year//100
    zeller=(day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    all_days=["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(all_days[zeller])
day2011()
