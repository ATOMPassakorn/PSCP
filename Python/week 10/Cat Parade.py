"""Cat Parade"""
def cat():
    """Cat Parade"""
    text=""
    catlist=[]
    countlist=[]
    catcount=[]
    dog="IT'S A DOG"
    while text!="END":
        text=input()
        if text!="END":
            catlist.extend(text.split(","))
    while dog in catlist:
        index=catlist.index(dog)
        if index:
            del catlist[index]
            del catlist[index-1]
        else:
            del catlist[index]
    for i in catlist:
        if i not in catcount:
            catcount.append(i)
            countlist.append(catlist.count(i))
    catlist.append(countlist)
    print(catlist)
cat()
