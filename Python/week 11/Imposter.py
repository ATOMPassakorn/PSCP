"""Impostor"""
import json
def among():
    """Impostor"""
    player=""
    player_now={}
    player_die={}
    while player!="Start":
        player=input()
        if player=="Start":
            break
        player_now.update(json.loads(player))
    die=""
    while die!="End":
        die=input()
        if die=="End":
            break
        if die in player_now:
            die_player=player_now.pop(die)
            player_die[die]=die_player
    print(f"{list(player_now.values()).count("Impostor")} Impostor Remains")
    print("***Alive***")
    for i,j in sorted(player_now.items()):
        print(f"{i} : {j}")
    print("***Dead***")
    for i,j in sorted(player_die.items()):
        print(f"{i} : {j}")
among()
