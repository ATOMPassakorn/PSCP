"""RockPaperScissor"""
def rps():
    """RockPaperScissor"""
    fight=input()
    a_point=0
    b_point=0
    for i in range(0,len(fight),2):
        match_won=fight[i:i+2]
        if match_won in ("RS","SP","PR"):
            a_point+=1
        elif match_won in ("SR","PS","RP"):
            b_point+=1
    if a_point>b_point:
        print(f"A win {a_point}-{b_point}")
    elif b_point>a_point:
        print(f"B win {b_point}-{a_point}")
    elif a_point == b_point:
        print(f"DRAW {a_point}")
rps()
