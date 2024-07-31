"""BrickBridge"""
def brick():
    """BrickBridge"""
    a=int(input())
    b=int(input())
    goal=int(input())
    ans=goal%5
    if a>b and b*5+a>=goal:
        if b*5>goal or goal-a>b*5:
            print(ans)
        else:
            print(goal-(b*5))
    elif a>=ans and goal<=b*5:
        print(ans)
    else:
        print(-1)
brick()
