"""Kabata"""
def kabata():
    """Kabata"""
    number=int(input())
    for _ in range(number):
        text=input()
        while any(sub in text for sub in ("baka", "bakka", "ba", "ka", "ta")):
            text = text.replace("baka","")
            text = text.replace("bakka","")
            text = text.replace("ba","")
            text = text.replace("ka","")
            text = text.replace("ta","")
    if not text:
        print("yes")
    else:
        print("no")
kabata()
