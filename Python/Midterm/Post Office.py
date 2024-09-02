"""Post Office"""
def post():
    """Post Office"""
    n=int(input())
    m=int(input())
    total=0
    for _ in range(n):
        n=float(input())
        total+=13
        if 0 <= n <= 10:
            total+=16
        elif 10 < n <= 20:
            total+=18
        elif 20 < n <= 100:
            total+=23
        elif 100 < n <= 250:
            total+=28
        elif 250 < n <= 500:
            total+=33
        elif 500 < n <= 1000:
            total+=48
        elif 1000 < n <= 2000:
            total+=68
    for _ in range(m):
        m=float(input())
        total+=15
        if 0 <= m <= 500:
            total+=45
        elif 500 < m <= 1000:
            total+=55
        elif 1000 < m <= 2000:
            total+=70
    print(total)
post()
