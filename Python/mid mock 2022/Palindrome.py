"""Palindrome"""
def palindrom():
    """Palindrome"""
    n=int(input())
    time=input()
    count=0
    hour=int(time[0:time.find(":")])
    manute=int(time[time.find(":")+1:])
    while count<n:
        manute += 1
        if manute == 60:
            manute = 0
            hour += 1
        if hour == 24:
            hour = 0
        time_now=f"{hour}{manute:02d}"
        if time_now==time_now[::-1]:
            print(f"{hour}:{manute:02d}")
            count+=1
palindrom()
