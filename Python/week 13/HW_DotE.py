"""HW_DotE"""
import math as m
def dota():
    """HW_DotE"""
    player=int(input())
    ways = 0
    if not player%2:
        choose = player//2
        ways = m.comb(player,choose)
    else:
        choose = player//2
        ways = m.comb(player,choose)+m.comb(player,choose+1)
    print(ways)
dota()
