"""Counting Stars"""
def stars():
    """Counting Stars"""
    text=input()
    comet=0
    shooting=0
    const=0
    i=0
    while i < (len(text)-1):
        if text[i]+text[i+1] in ("~*","*~"):
            comet+=1
            i+=2
        elif text[i]+text[i+1] == "*/":
            shooting+=1
            i+=2
        elif text[i]+text[i+1] == "**":
            const+=1
            i+=2
        else:
            i+=1
    if comet or const or shooting:
        print(f"constellation: {const}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting}")
    else:
        print("Tonight is a quiet night.")
stars()
