"""Netflix"""
def func_pre(numsame, numload):
    """premium"""
    ans = max(numsame, numload) // 4
    ans1 = max(numsame, numload) % 4
    if ans1 > 0:
        ans += 1
    print(f"Premium x {ans}")
    print(f"Total = {ans * 419} THB")
def func_std(numsame, numload):
    """standard"""
    howmany = 0
    rnd = 0
    howmuch = 0
    if max(numsame, numload) > 2:
        ans = max(numsame, numload) // 4
        if max(numsame, numload) - (ans * 4) == 3:
            ans += 1
            rnd = 1
        print(f"Premium x {ans}")
        howmany = max(numsame, numload) - (ans * 4)
        howmuch = ans * 419
        rnd += 1
    if howmany > 0 or not rnd:
        if not rnd :
            ans = max(numsame, numload) // 2
            print(f"Standard x {ans}")
            print(f"Total = {ans * 349} THB")
        else:
            ans = howmany // 2
            ans1 = howmany % 2
            if ans1 > 0:
                ans += 1
            print(f"Standard x {ans}")
            howmuch = howmuch + (ans * 349)
            print(f"Total = {howmuch} THB")
    else:
        print(f"Total = {howmuch} THB")
def func_bsc(numsame, numload):
    """basic"""
    ans = 0
    howmuch = 0
    howmany = 0
    rnd = 0
    if max(numsame, numload) > 2:
        ans = max(numsame, numload) // 4
        if max(numsame, numload) - (ans * 4) == 3:
            ans += 1
            rnd = 1
        print(f"Premium x {ans}")
        howmany = max(numsame, numload) - (ans * 4)
        howmuch = ans * 419
        rnd = 1
    if howmany > 1 or (max(numsame, numload) > 1 and not rnd):
        if not rnd:
            ans = max(numsame, numload) // 2
            print(f"Standard x {ans}")
            print(f"Total = {ans * 349} THB")
            howmany = ans - (ans * 2)
            howmuch = howmuch + (ans * 349)
            rnd = 2
        else:
            ans = howmany // 2
            print(f"Standard x {ans}")
            howmany = howmany - (ans * 2)
            howmuch = howmuch + (ans * 349)
            rnd = 1
    if howmany > 0 or not rnd:
        if not rnd:
            ans = max(numsame, numload)
            print(f"Basic x {ans}")
            print(f"Total = {ans * 279} THB")
        else:
            print(f"Basic x {howmany}")
            howmuch = howmuch + (howmany * 279)
            print(f"Total = {howmuch} THB")
    elif rnd == 1:
        print(f"Total = {howmuch} THB")
def func_mb(numsame, numload):
    """mobile"""
    ans = max(numsame, numload)
    print(f"Mobile x {ans}")
    print(f"Total = {ans * 99} THB")
def main():
    """netflix"""
    numsame = int(input())
    numload = int(input())
    ulimited = input().lower()
    inmobile = input().lower()
    intv = input().lower()
    nhd = input().lower()
    uhd = input().lower()
    if not max(numsame, numload):
        print("What do you want?\nTotal = 0")
    elif uhd == "yes":
        func_pre(numsame, numload)
    elif nhd == "yes":
        func_std(numsame, numload)
    elif intv == "yes":
        func_bsc(numsame, numload)
    elif ulimited != "1" and inmobile != "1":
        func_mb(numsame, numload)
main()
