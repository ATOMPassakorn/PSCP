"""Saitama"""
import math as m
def workout():
    """work out for P'Sai"""
    wid_goal = int(input())
    sit_goal = int(input())
    squad_goal = int(input())
    run_goal = int(input())
    wid = int(input())
    sit = int(input())
    run = int(input())
    squad = int(input())
    wid_day = m.ceil(wid_goal / wid)
    sit_day = m.ceil(sit_goal / sit)
    squad_day = m.ceil(squad_goal / squad)
    run_day = m.ceil(run_goal / run)
    most = wid_day
    if sit_day > most:
        most = sit_day
    if squad_day > most:
        most = squad_day
    if run_day > most:
        most = run_day
    print(most)
workout()
