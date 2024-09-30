"""PongYa"""
def pongya():
    """PongYa"""
    number=int(input())
    check=str(number)[-1]
    if not number%3 or check=="3":
        print("PONG")
    else:
        print(number)
pongya()
