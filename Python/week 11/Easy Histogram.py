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
            if i in textdict:
                textdict[i]+=1
            else:
                textdict[i]=1
    sorted_text=sorted(textdict.keys(),key=sort_key)
    for i in sorted_text:
        print(f"{i} = {textdict[i]}")
histogram()
