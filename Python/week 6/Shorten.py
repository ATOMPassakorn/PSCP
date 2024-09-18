"""Shorten"""
def shorten():
    """Shorten"""
    num=""
    ans=""
    start=None
    end=None
    while num!=-1:
        num=input().strip()
        if num == "-1":
            break
        num=int(num)
        if start is None:
            start=num
            end=num
        elif num == end+1:
            end=num
        else:
            if start==end:
                ans+=f"{start}, "
            else:
                ans+=f"{start}-{end}, "
            start=num
            end=num
    if start is not None:
        if start==end:
            ans+=f"{start}"
        else:
            ans+=f"{start}-{end}"
    print(ans)
shorten()
