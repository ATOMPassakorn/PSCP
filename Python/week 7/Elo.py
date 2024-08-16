"""Elo"""
def elo():
    """Elo"""
    ra=int(input())
    rb=int(input())
    choose=input()
    if choose=="A":
        ea=1/(1+10**((rb-ra)/400))
    else:
        ea=1/(1+10**((ra-rb)/400))
    print(f"{ea:.2f}")
elo()
