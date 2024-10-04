"""Heads and Legs"""
def animal():
    """Heads and Legs"""
    all_ani=int(input())
    leg=int(input())
    rabbit=(leg-2*all_ani)//2
    bird=all_ani-rabbit
    if rabbit<0 or bird<0 or leg!=(4*rabbit+2*bird):
        print("Impossible")
    else:
        print(f"{rabbit} {bird}")
animal()
