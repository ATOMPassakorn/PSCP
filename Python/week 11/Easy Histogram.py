"""Easy Histogram"""
def sort_key(x):
    """sort"""
    return (x.lower(),x.isupper())
def histogram():
    """histogram"""
    text = input()
    textdict = {}
    for i in text:
        if i != " ":
            textdict[i]=textdict.get(i,0)+1
    print(textdict.values())
histogram()
