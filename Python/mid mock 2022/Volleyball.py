"""Volleyball"""
def check_set(a, b, awin, bwin, sets):
    """check_set"""
    if a == 25 and b <= 23:
        awin += 1
        sets += 1
        print(f"Set {sets}: A ({a}) | B ({b})")
        a = 0
        b = 0
    elif b == 25 and a <= 23:
        bwin += 1
        sets += 1
        print(f"Set {sets}: A ({a}) | B ({b})")
        a = 0
        b = 0
    elif a >= 24 and b >= 24:
        if b - a == 2:
            bwin += 1
            sets += 1
            print(f"Set {sets}: A ({a}) | B ({b})")
            a = 0
            b = 0
        elif a - b == 2:
            awin += 1
            sets += 1
            print(f"Set {sets}: A ({a}) | B ({b})")
            a = 0
            b = 0
    return a, b, awin, bwin, sets
def check_final_set(a, b, awin, bwin, sets):
    """check final set"""
    if a >= 15 and b <= 13:
        awin += 1
        sets += 1
        print(f"Set {sets}: A ({a}) | B ({b})")
        a = 0
        b = 0
    elif b >= 15 and a <= 13:
        bwin += 1
        sets += 1
        print(f"Set {sets}: A ({a}) | B ({b})")
        a = 0
        b = 0
    elif a >= 14 and b >= 14:
        if b - a == 2:
            bwin += 1
            sets += 1
            print(f"Set {sets}: A ({a}) | B ({b})")
            a = 0
            b = 0
        elif a - b == 2:
            awin += 1
            sets += 1
            print(f"Set {sets}: A ({a}) | B ({b})")
            a = 0
            b = 0
    return a, b, awin, bwin, sets
def volleyball():
    """Volleyball Set"""
    volley = input()
    a = 0
    b = 0
    sets = 0
    awin = 0
    bwin = 0
    for i in volley:
        if i == "A":
            a += 1
        else:
            b += 1
        a, b, awin, bwin, sets = check_set(a, b, awin, bwin, sets)
        if awin == 3 or bwin == 3:
            break
        if sets == 4:
            a, b, awin, bwin, sets = check_final_set(a, b, awin, bwin, sets)
            if awin == 3 or bwin == 3:
                break
    if awin == 3:
        print(f"A won {awin}:{bwin} set")
    elif bwin == 3:
        print(f"B won {bwin}:{awin} set")
    else:
        print(f"Set {sets + 1}: A ({a}) | B ({b})")
        print("The game has not finished yet.")
volleyball()
