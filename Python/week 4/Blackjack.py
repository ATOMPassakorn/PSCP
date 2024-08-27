"""Blackjack"""
def blackjack():
    """Blackjack"""
    num=int(input())
    score=0
    aces=0
    for _ in range(num):
        card=input()
        if card in ("J","Q","K"):
            score+=10
        elif card=="A":
            score+=11
            aces+=1
        else:
            score+=int(card)
    while score>21 and aces:
        score-=10
        aces-=1
    print(score)
blackjack()
