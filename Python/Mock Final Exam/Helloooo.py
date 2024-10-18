"""Helloooo"""
def eng():
    """Helloooo"""
    text=input()
    vowel=["a","e","i","o","u"]
    found=[]
    ans=""
    for i in text:
        if i in vowel:
            found.append(i)
    if found:
        last=found[-1]
        for i,j in enumerate(text):
            if j==last and text[i:].count(last)==1:
                ans+=text[i]*4
            else:
                ans+=text[i]
        print(ans)
    else:
        print(text)
eng()
