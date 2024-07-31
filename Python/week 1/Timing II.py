"""Timing II"""
def time():
    """Timing II"""
    num=int(input())
    sec=num%60
    minute=(num//60)%60
    hour=(num//3600)%24
    day=num//86400
    if day>9999:
        print("ERR_:__:__:__")
    else:
        print(f"{day:>04}:{hour:>02}:{minute:>02}:{sec:>02}")
time()
