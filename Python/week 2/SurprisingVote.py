"""SurprisingVote"""
def surprise():
    """SurprisingVote"""
    goal=float(input())
    high=float(input())
    score=max(0,goal-high*2)
    if high-score<=2:
        print("Not surprising")
    else:
        print("Surprising")
surprise()
