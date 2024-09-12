"""Cat Parade"""
def cat():
    """Cat Parade"""
    text=""
    catlist=[]
    catcount=[]
    while text!="END":
        text=input()
        if text!="END":
            catlist.extend(text.split(", "))
    while "IT'S A DOG" in catlist:
        index=catlist.index("IT'S A DOG")
        del catlist[index]
        del catlist[index-1]
    for i in catlist:
        if i not in catcount:
            catcount.append(i)
    catcount.sort()
    for i in catcount:
        print(f"{i} {catlist.index(i)+1} {catlist.count(i)}")
cat()
