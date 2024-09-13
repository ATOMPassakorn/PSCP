"""Easy Histogram No Dict"""
def sort_key(x):
    """sort"""
    return (x.lower(),x.isupper())
def histogram():
    """Easy Histogram No Dict"""
    text=input()
    textlist=[]
    textnew=[]
    length=len(text)
    for i in range(length):
        if text[i]!=" ":
            textlist.append(text[i])
    for i in textlist:
        if i not in textnew:
            textnew.append(i)
    textnew.sort(key=sort_key)
    for i in textnew:
        print(f"{i} = {textlist.count(i)}")
histogram()
