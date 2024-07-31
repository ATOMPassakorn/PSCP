"""time"""
def com():
    """time"""
    start=492137954293754252786
    millisec=start
    seconds=millisec//1000
    millisec=millisec%1000
    minutes=seconds//60
    seconds=seconds%60
    hour=minutes//60
    minutes=minutes%60
    day=hour//24
    hour=hour%24
    print(day,hour,minutes,seconds,millisec)
com()
